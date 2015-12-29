from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, flt, nowdate
from frappe import _, throw

def submit_event(doc, method):
    make_po_for_manufacturer(doc)
    make_po_for_fabric_supplier(doc)

def make_po_for_manufacturer(doc):
    for data in doc.items:
        if data.manufacturer_name and cint(data.make_po_for_manufacturer) == 1:
            name = frappe.db.get_value('Purchase Order', {'supplier': data.manufacturer_name, 'sales_order': doc.name}, 'name')
            args = {'item_code': data.item_code, 'qty': data.qty, 'warehouse': data.warehouse, 'item_name': data.item_name, 'uom': data.stock_uom,
                    'schedule_date': nowdate(), 'conversion_factor': frappe.db.get_value("UOM Conversion Detail",{'parent': data.item_code
                    , 'uom': data.stock_uom}, "conversion_factor")}
            if name:
                doc = frappe.get_doc('Purchase Order', name)
                add_po_item(doc, args)
            else:
                doc = frappe.get_doc({
                    'doctype': 'Purchase Order',
                    'supplier': data.manufacturer_name,
                    'sales_order': doc.name
                })
                add_po_item(doc, args)
            doc.save()

def make_po_for_fabric_supplier(doc):
    for data in doc.items:
        if data.fabric_supplier and data.fabric_item_code and cint(data.make_po_for_supplier) == 1:
            name = frappe.db.get_value('Purchase Order', {'supplier': data.fabric_supplier, 'sales_order': doc.name}, 'name')
            args = {'item_code': data.fabric_item_code, 'qty': data.fabric_qty, 'warehouse': data.fabric_warehouse, 'item_name': data.fabric_item_name, 'uom': data.uom,
                    'schedule_date': nowdate(), 'conversion_factor': frappe.db.get_value("UOM Conversion Detail",{'parent': data.fabric_item_code
                    , 'uom': data.uom}, "conversion_factor")}
            if name:
                doc = frappe.get_doc('Purchase Order', name)
                add_po_item(doc, args)
            else:
                doc = frappe.get_doc({
                    'doctype': 'Purchase Order',
                    'supplier': data.manufacturer_name,
                    'sales_order': doc.name
                })
                add_po_item(doc, args)
            doc.save()

def add_po_item(doc, args):
    doc.append('items', args)

def cancel_event(doc, method):
    check_po_link(doc)

def check_po_link(doc):
    for data in frappe.db.get_values('Purchase Order', {'sales_order': doc.name, 'docstatus': '<>2'}, 'name', as_dict=1):
        throw(_('Error: Sales Order {0}, is linked with Purchase Order {1}, delete Purchase Order first').format(doc.name, data.name))
