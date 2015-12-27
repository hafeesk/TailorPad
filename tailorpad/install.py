from __future__ import unicode_literals
import frappe

def after_install():
    update_homepage()

def hide_homepage():
    frappe.db.sql("""update `tabSingles` set value = 'login'
    where field='home_page' and doctype = 'Website Settings'""")
