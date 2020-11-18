# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "jwt_frappe"
app_title = "Jwt Frappe"
app_publisher = "ahmadragheb"
app_description = "auth with token for mobile and frontend applications "
app_icon = "octicon octicon-file-directory"
app_color = "pink"
app_email = "Ahmedragheb75@gmail.com"
app_license = "MIT"



on_session_creation = "jwt_frappe.on_session_creation"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jwt_frappe/css/jwt_frappe.css"
# app_include_js = "/assets/jwt_frappe/js/jwt_frappe.js"

# include js, css files in header of web template
# web_include_css = "/assets/jwt_frappe/css/jwt_frappe.css"
# web_include_js = "/assets/jwt_frappe/js/jwt_frappe.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "jwt_frappe.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jwt_frappe.install.before_install"
# after_install = "jwt_frappe.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jwt_frappe.notifications.get_notification_config"

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
# 		"jwt_frappe.tasks.all"
# 	],
# 	"daily": [
# 		"jwt_frappe.tasks.daily"
# 	],
# 	"hourly": [
# 		"jwt_frappe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jwt_frappe.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jwt_frappe.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jwt_frappe.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jwt_frappe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "jwt_frappe.task.get_dashboard_data"
# }
