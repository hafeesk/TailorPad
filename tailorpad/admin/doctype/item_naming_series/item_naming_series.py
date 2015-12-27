# -*- coding: utf-8 -*-
# Copyright (c) 2015, Lagan Jaiswal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ItemNamingSeries(Document):
	def before_save(self):
		self.add_to_naming_series()

	def add_to_naming_series(self):
		ps_exists = self.get_ps_data()
		if ps_exists and self.name!='ITEM-':
			value = ps_exists.value +'\n'+ self.name
			self.update_property_setter(value, ps_exists.name)

	def on_trash(self):
		self.delete_from_naming_series()

	def delete_from_naming_series(self):
		query = "select name from `tabItem Naming Series` where name!='{0}'".format(self.name)
		data = [d.name for d in frappe.db.sql(query, as_dict=1)]
		ps_exists = self.get_ps_data()
		value = "\n".join(data) if data else ""
		if ps_exists:
			self.update_property_setter(value, ps_exists.name)

	def get_ps_data(self):
		return frappe.db.get_value('Property Setter',
			{'field_name': 'naming_series', 'doc_type': 'Item', 'property': 'options'}, '*', as_dict=1)

	def update_property_setter(self, value, name):
		ps_name = frappe.get_doc('Property Setter', name)
		ps_name.value = value
		ps_name.save()
		frappe.clear_cache(doctype='Item')
