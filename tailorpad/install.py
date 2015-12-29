from __future__ import unicode_literals
import frappe

def after_install(args=None):
    hide_homepage()

def hide_homepage():
    frappe.db.sql("""update `tabSingles` set value = 'login'
    where field='home_page' and doctype = 'Website Settings'""")

    item_groups = ['Tailoring', 'Fabric', 'Merchandise', 'Fabric Swatch Item']
    for item_group in item_groups:
	    if not frappe.db.get_value('Item Group', item_group, 'name'):
	    	gp = frappe.new_doc('Item Group')
	    	gp.item_group_name = item_group
	    	gp.parent_item_group = 'All Item Groups'
	    	gp.is_group = 'No'
	    	gp.save(ignore_permissions=True)
	    	# group = frappe.get_doc({
	    	# 	'doctype': 'Item Group',
	    	# 	'parent_item_group': ' All Item Groups',
	    	# 	'name': item_group
	    	# })

	    	# group.save(ignore_permissions=True)
