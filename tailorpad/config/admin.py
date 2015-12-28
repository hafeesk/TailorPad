from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
                {
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"name": "Supplier",
					"description": _("Supplier database."),
				}
			]
		},
		{
			"label": _("Setup"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Size",
					"description": _("Size database.")
				},
				{
					"type": "doctype",
					"name": "Width",
					"description": _("Width database.")
				},
				{
					"type": "doctype",
					"name": "Style",
					"description": _("Style database.")
				},
				{
					"type": "doctype",
					"name":"Style Template",
					"label": _("Style Template"),
					"description": _("Template of differnt types of style.")
				},
				{
					"type": "doctype",
					"name": "Measurement Template",
                    "label": _("Measurement Template"),
					"description": _("Template of differnt types of measurement.")
				},
				{
					"type": "doctype",
					"name": "Work Order",
                    "label": _("Work Order"),
					"description": _("Orders released for production.")
				},
			]
		},
	]
