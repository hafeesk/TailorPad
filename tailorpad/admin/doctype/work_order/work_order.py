# -*- coding: utf-8 -*-
# Copyright (c) 2015, Lagan Jaiswal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt
from frappe.model.document import Document

class WorkOrder(Document):
	def validate(self):
		self.calculate_extra_style_cost()

	def calculate_extra_style_cost(self):
		extra_style = [flt(style_data.cost_to_customer) for style_data in self.style_fields]
		self.extra_style_cost = sum(extra_style)
