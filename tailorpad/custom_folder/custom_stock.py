from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt
from frappe import _, throw

@frappe.whitelist()
def fetch_measurement(measurement_template):
    return frappe.db.get_values('Measurement Fields', {'parent': measurement_template}, '*', as_dict=1, debug=1)

@frappe.whitelist()
def fetch_style(style_template):
    return frappe.db.get_values('Style fields', {'parent': style_template}, '*', as_dict=1, debug=1)
