import uuid
from flask.views import MethodView
from flask import jsonify, request
from app.models import Request,BIBLESTUDIES,BibleStudy,REQUESTS


class RequestAPI(MethodView):
    """This class-based view for requesting to join a biblestudy."""
    @staticmethod
    def post(biblestudy_id):
        '''Method for a post request'''
        biblestudy_id = uuid.UUID(biblestudy_id)
        res = Request.request_biblestudy(biblestudy_id)
        if res == "You have successfully accepted the biblestudy_request.":
            return jsonify({'msg': res}), 201

