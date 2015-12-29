from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt
from frappe import _, throw, msgprint

def submit_event(doc, method):
    make_work_order(doc)

def make_work_order(doc):
    for args in doc.items:
        if args.item_group == 'Tailoring':
            prepare_data_for_wo(doc, args)

def prepare_data_for_wo(doc, args):
    quantities = args.split_qty.split(',') if args.split_qty else [args.qty]
    item_data = frappe.db.get_values('Product Bundle Item',
                {'parent': args.item_code}, ['item_code', 'parent'], as_dict=1) or [{'parent': args.item_code,
                'item_code': args.item_code}]

    for items in item_data:
        for qty in quantities:
            create_work_order(doc, args, items, qty)

def create_work_order(doc, args, items, qty):
    wo = frappe.get_doc({
        'doctype': 'Work Order',
        'sales_order': doc.name,
        'parent_item_code': items.parent,
        'item_code': items.item_code,
        'item_name': frappe.db.get_value('Item', items.item_code, 'item_group'),
        'item_qty': qty,
        'fabric_code': args.fabric_item_code,
        'customer': doc.customer,
        'customer_name': doc.customer_name
    })
    get_measurement_fields(wo, items.item_code)
    get_style_fields(wo, items.item_code)
    wo.save()

def get_measurement_fields(wo, item_code):
    for d in frappe.db.get_values('Measurement Fields', {'parent': item_code}, '*', as_dict=1):
        wo.append("measurement_fields",
            {"measurement_field": d.measurement_field,
             "measurement_value": d.measurement_value,
             "note": d.note,
             "image": d.image,
             "image_view": d.image_view})

def get_style_fields(wo, item_code):
    for d in frappe.db.get_values('Style fields', {'parent': item_code, 'default': 1}, '*', as_dict=1):
        wo.append("style_fields",
            {"style_field": d.style_field,
             "style_name": d.style_name,
             "note": d.note,
             "image": d.image,
             "image_view": d.image_view})

def cancel_event(doc, method):
    check_wo_link(doc)

def check_wo_link(doc):
    for data in frappe.db.get_values('Work Order', {'sales_order': doc.name, 'docstatus': '<>2'}, 'name', as_dict=1):
        throw(_('Error: Sales Order {0}, is linked with Work Order {1}, delete Work Order first').format(doc.name, data.name))

@frappe.whitelist()
def get_supplier(item_code):
    return frappe.db.get_value('Item', item_code, ['default_supplier', 'default_warehouse'], as_dict=1)

def get_fabric(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql(""" select name, item_name from tabItem where (item_group = "Fabric" or item_group = "Fabric Swatch Item") and
        (name like "%%%(txt)s%%" or item_name like "%%%(txt)s%%") limit %(start)s, %(page_len)s"""%{'txt': txt, 'start': start, 'page_len': page_len})

@frappe.whitelist()
def get_fabric_qty(parent, size, width):
    return frappe.db.get_value('Size Details', {'parent': parent, 'size': size, 'width': width}, 'fabric_qty', as_dict=1)
