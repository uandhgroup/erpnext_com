# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "internal_aireldentalchairs_com"
app_title = "Internal ADI"
app_publisher = "Frappe"
app_description = "Internal.Aireldentalchairs.Com website"
app_icon = "fa fa-globe"
app_color = "black"
app_email = "web@uandh.in"
app_url = "https://Internal.Aireldentalchairs.Com"
app_version = "0.0.1"
hide_in_installer = True

website_context = {
	"brand_html": "<img class='mr-2 d-inline-block align-top' src='/assets/internal_aireldentalchairs_com/img/ai-logo-blue.svg' />Internal Airel Dental",
	"top_bar_items": [
		{"label": "Pricing", "url": "/pricing", "right":1},
		{"label": "Support", "url": "/support", "right":1},
		{"label": "Learn", "url": "/learn", "right":1},
		{"label": "Sign Up", "url": "/signup", "right":1},
		{"label": "Industries", "right":1, "child_items": [
			{"label": "Services", "url":"/services"},
			{"label": "Manufacturing", "url":"/manufacturing"},
			{"label": "Retail", "url":"/retail"},
			{"label": "Distribution", "url":"/distribution"},
			{"label": "Education", "url":"/education"},
			{"label": "Non Profit", "url":"/non-profit"},
			{"label": "Doctor Financing", "url":"/doctor_financing"},
		]},
		{"label": "About", "url": "/about", "right":1},
	],
	"hide_login": 1,
	"favicon": "/assets/internal_aireldentalchairs_com/img/ai-logo-blue.png"
}

website_redirects = [
	{'source': '/compare', 'target': 'https://aireldentalchairs.com/contribute' },
	{'source': '/benefits', 'target': '/about' },
	{'source': '/features', 'target': '/learn' },
	{'source': '/download', 'target': 'https://aireldentalchairs.com/get-started' },
	{'source': '/faq', 'target': 'https://aireldentalchairs.com/faq' },
	{'source': '/open-learn', 'target': 'https://aireldentalchairs.com/open-learn' },
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/internal_aireldentalchairs_com/css/internal_aireldentalchairs_com.css"
# app_include_js = "/assets/internal_aireldentalchairs_com/js/internal_aireldentalchairs_com.js"

# include js, css files in header of web template
web_include_css = "/assets/internal_aireldentalchairs_com/css/custom.css"
web_include_js = "/assets/internal_aireldentalchairs_com/js/payment.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

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

# before_install = "internal_aireldentalchairs_com.install.before_install"
# after_install = "internal_aireldentalchairs_com.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "internal_aireldentalchairs_com.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"internal_aireldentalchairs_com.tasks.all"
# 	],
# 	"daily": [
# 		"internal_aireldentalchairs_com.tasks.daily"
# 	],
# 	"hourly": [
# 		"internal_aireldentalchairs_com.tasks.hourly"
# 	],
# 	"weekly": [
# 		"internal_aireldentalchairs_com.tasks.weekly"
# 	]
# 	"monthly": [
# 		"internal_aireldentalchairs_com.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "internal_aireldentalchairs_com.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "internal_aireldentalchairs_com.event.get_events"
# }

fixtures = ["Contact Us Settings"]
