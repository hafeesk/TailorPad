# -*- coding: utf-8 -*-
# Copyright (c) 2015, Lagan Jaiswal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt
from frappe import _, throw
from frappe.model.document import Document

class WorkOrder(Document):
	def validate(self):
		self.calculate_extra_style_cost()

	def calculate_extra_style_cost(self):
		extra_style = [flt(style_data.cost_to_customer) for style_data in self.style_fields]
		self.extra_style_cost = sum(extra_style)

	def get_measurement_from_wo(self):
		if self.import_measurement_from_work_order:
			self.set('measurement_fields',[])
			measurement_fields = frappe.db.get_values('Measurement Fields', {'parent': self.import_measurement_from_work_order}, '*', as_dict=1)
			for measurement in measurement_fields:
				wo_meaurement = self.append('measurement_fields', {})
				for key, value in measurement.items():
					setattr(wo_meaurement, key, value)
		return True

	def get_style_from_wo(self):
		if self.import_style_from_work_order:
			self.set('style_fields',[])
			style_fields = frappe.db.get_values('Style fields', {'parent': self.import_style_from_work_order}, '*', as_dict=1)
			for style in style_fields:
				wo_style = self.append('style_fields', {})
				for key, value in style.items():
					setattr(wo_style, key, value)
		return True

	def on_submit(self):
		if not self.measured_by:
			throw(_('Measured By is mandatory field'))

def work_orderlink(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql(""" select name, measured_by, modified from `tabWork Order`
							where (name like '%%%(txt)s%%' or measured_by like '%%%(txt)s%%') and name <> '%(work_order)s'
							limit %(start)s, %(page_len)s"""%{'txt': txt, 'start': start, 'page_len': page_len, 'work_order': filters.get('work_order')})
