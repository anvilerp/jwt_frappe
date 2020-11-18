# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.utils import cint

__version__ = '1.0.0'

def on_session_creation(login_manager):
  from jwt_frappe.utils.auth import make_jwt
  if frappe.form_dict.get('use_jwt') and cint(frappe.form_dict.get('use_jwt')):
    frappe.local.response['token'] = make_jwt(
        login_manager.user, frappe.flags.get('jwt_expire_on'))
    frappe.flags.jwt_clear_cookies = True


@frappe.whitelist()
def get_logged_user():
  user = frappe.session.user