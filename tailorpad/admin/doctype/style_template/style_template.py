# -*- coding: utf-8 -*-
# Copyright (c) 2015, Lagan Jaiswal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr
from frappe.model.document import Document

class StyleTemplate(Document):
	def validate(self):
		self.duplicate_style_default()

	def duplicate_style_default(self):
		style_dict = {}
		for style in self.style_fields:
			if cint(style.default) == 1 and style_dict.count(style.style_field):
				pass
