from __future__ import unicode_literals
import frappe
from frappe import _


def get_data():
    return [
        {
            "module_name": "Member Registration",
            "category": "Modules",
            "label": _("Member Registration"),
            "color": "grey",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Member Registration"),
            "description": "Member database."
        },
    ]
