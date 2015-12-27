from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_clubbed_product(source_name, target_doc=None):
	def postprocess(source, doc):
		doc.new_item_code = source.name

	doc = get_mapped_doc("Item", source_name, {
		"Item": {
			"doctype": "Product Bundle",
			"validation": {
				"is_stock_item": ["=", 0]
			}
		}
	}, target_doc, postprocess)

	return doc
