from __future__ import unicode_literals
import frappe
from frappe import _


def get_data():
    return [
        {
            "module_name": "Member Registration",
            "category": "module",
            "label": _("Member Registration"),
            "color": "grey",
            "reverse": 1,
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "description": "Todos, notes, calendar and newsletter."
        },
    ]
