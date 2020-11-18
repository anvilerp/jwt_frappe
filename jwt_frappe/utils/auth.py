import random

import frappe
import jwt
from frappe import _
from frappe.auth import LoginManager
from frappe.utils import cint
from frappe.utils.password import check_password, passlibctx, update_password



def get_linked_user(id_type, id):
  """
  Returns the user associated with the details
  :param id_type: either 'mobile' or 'email'
  :param id: the email/mobile
  """
  if id_type not in ("mobile", "sms", "email"):
    frappe.throw(f"Invalid id_type: {id_type}")

  if id_type in ("mobile", "sms"):
    id_type = "mobile_no"

  return frappe.db.get_value("User", {id_type: id})





@frappe.whitelist(allow_guest=True)
def get_token(user, pwd, expire_on=None, device=None):
  """
  Get the JWT Token
  :param user: The user in ctx
  :param pwd: Pwd to auth
  :param expire_on: yyyy-mm-dd HH:mm:ss to specify the expiry
  :param device: The device in ctx
  """
  if not frappe.db.exists("User", user):
    raise frappe.ValidationError(_("Invalide User"))

  from frappe.sessions import clear_sessions
  login = LoginManager()
  login.check_if_enabled(user)
  if not check_password(user, pwd):
    login.fail('Incorrect password', user=user)
  login.login_as(user)
  login.resume = False
  login.run_trigger('on_session_creation')
  clear_sessions(user, True, device)
  if expire_on:
    frappe.flags.jwt_expire_on = expire_on


def make_jwt(user, expire_on=None, secret=None):
  if not frappe.session.get('sid') or frappe.session.sid == "Guest":
    return

  if frappe.session.user == frappe.session.sid:
    # active via apikeys/bearer tokens, no real session inplace
    from frappe.sessions import Session
    user_info = frappe.db.get_value(
        "User", frappe.session.user,
        ["user_type", "first_name", "last_name"], as_dict=1)
    frappe.local.session_obj = Session(
        user=frappe.session.user, resume=False,
        full_name=user_info.first_name, user_type=user_info.user_type)
    frappe.local.session = frappe.local.session_obj.data

  if not secret:
    secret = frappe.utils.password.get_encryption_key()
  if expire_on and not isinstance(expire_on, frappe.utils.datetime.datetime):
    expire_on = frappe.utils.get_datetime(expire_on)

  id_token_header = {
      "typ": "jwt",
      "alg": "HS256"
  }
  id_token = {
      "sub": user,
      "ip": frappe.local.request_ip,
      "sid": frappe.session.get('sid')
  }
  if expire_on:
    id_token['exp'] = int(
        (expire_on - frappe.utils.datetime.datetime(1970, 1, 1)).total_seconds())
  token_encoded = jwt.encode(
      id_token, secret, algorithm='HS256', headers=id_token_header).decode("ascii")
  frappe.flags.jwt = token_encoded
  return token_encoded


@frappe.whitelist()
def get_jwt_token():
  """
  Get jwt token for the active user
  """
  return make_jwt(user=frappe.session.user)
