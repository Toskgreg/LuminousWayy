"""This module handle the registering of the REQUEST_APP blue_print and
 adding the adds the url rule"""
from flask import Blueprint
from app.request.api import RequestAPI
REQUEST_APP = Blueprint('REQUEST_APP', __name__)

REQUEST_VIEW = RequestAPI.as_view('request_api')
REQUEST_APP.add_url_rule('/api/v1/biblestudies/<biblestudy_id>/request/',
                        view_func=REQUEST_VIEW, methods=['POST', ])
