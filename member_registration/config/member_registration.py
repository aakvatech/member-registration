from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Masters"),
            "icon": "fa fa-group",
            "items": [
                {
                    "type": "doctype",
                    "name": "Organisation",
                    "description": _("Organisation")
                },
                {
                    "type": "doctype",
                    "name": "Security Group",
                    "description": _("Security Group")
                },
                {
                    "type": "doctype",
                    "name": "Family",
                    "description": _("Family")
                },
            ]
        },
    ]
