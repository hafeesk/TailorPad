# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Tailorpad": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Tailorpad")
		},
		"Admin": {
			"color": "#981B77",
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"label": _("Admin")
		}
	}
