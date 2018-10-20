from flask import Blueprint
from app.biblestudy.api import BIBLESTUDYAPI

BIBLESTUDY_APP = Blueprint('BIBLESTUDY_APP', __name__)

BIBLESTUDY_VIEW = BIBLESTUDYAPI.as_view('biblestudy_api')
BIBLESTUDY_APP.add_url_rule('/api/v1/biblestudies/', defaults={'biblestudy_id': None},
                          view_func=BIBLESTUDY_VIEW, methods=['GET', ])

BIBLESTUDY_APP.add_url_rule(
    '/api/v1/biblestudies/<biblestudy_id>',
    view_func=BIBLESTUDY_VIEW,
    methods=[
        'GET',
    ])

BIBLESTUDY_APP.add_url_rule(
    '/api/v1/biblestudies/', view_func=BIBLESTUDY_VIEW, methods=['POST', ])
