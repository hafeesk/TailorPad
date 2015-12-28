# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "tailorpad"
app_title = "Tailorpad"
app_publisher = "Lagan Jaiswal"
app_description = "Tailoring Application"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "laganjaiswal@gmail.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tailorpad/css/tailorpad.css"
# app_include_js = "/assets/tailorpad/js/tailorpad.js"

# include js, css files in header of web template
web_include_css = "/assets/tailorpad/css/tailorpad.css"
# web_include_js = "/assets/tailorpad/js/tailorpad.js"

# Home Pages
# ----------

fixtures = ['Custom Field', 'Property Setter']

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tailorpad.install.before_install"
after_install = "tailorpad.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tailorpad.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_submit": ["tailorpad.custom_folder.custom_selling.submit_event", "tailorpad.custom_folder.custom_buying.submit_event"],
		"on_cancel": ["tailorpad.custom_folder.custom_selling.cancel_event", "tailorpad.custom_folder.custom_buying.cancel_event"]
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tailorpad.tasks.all"
# 	],
# 	"daily": [
# 		"tailorpad.tasks.daily"
# 	],
# 	"hourly": [
# 		"tailorpad.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tailorpad.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tailorpad.tasks.monthly"
# 	]
# }
doctype_js = {
    "User": ["custom_scripts/user.js"],
    "Item": ["custom_scripts/item.js"],
	"Sales Order": ["custom_scripts/sales_order.js"],
	"Quotation": ["custom_scripts/quotation.js"],
	"Sales Invoice": ["custom_scripts/sales_invoice.js"]
}


# Testing
# -------

# before_tests = "tailorpad.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tailorpad.event.get_events"
# }
