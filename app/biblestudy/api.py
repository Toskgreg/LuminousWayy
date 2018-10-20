"""This module handles BIBLESTUDYAPI class and its methods"""
import uuid
from flask.views import MethodView
from flask import jsonify, request, make_response
from app.models import BibleStudy,BIBLESTUDIES


class BIBLESTUDYAPI(MethodView):
    """This class based view handles biblestudy related methods"""
    @staticmethod
    def get(biblestudy_id):
        """Method for  get requests"""
        if biblestudy_id:
            biblestudy_id = uuid.UUID(biblestudy_id)
            biblestudy = BibleStudy.view_biblestudy_by_ID(biblestudy_id)
            return jsonify(biblestudy), 200
        else:
            biblestudies = BibleStudy.view_all_biblestudies()
            if BIBLESTUDIES == []:
                response = {
                    "msg": " There are no biblestudy_requestss at the moment"}
                return make_response(jsonify(response)), 200
            return jsonify(biblestudies), 200

    @staticmethod
    def post():
        '''Method for a post request'''
        data = request.json
        biblestudy_title = data["biblestudy_title"]
        biblestudy_description = data["biblestudy_description"]
        res = BibleStudy.ask_biblestudy(biblestudy_title, biblestudy_description)
        if res == "Your biblestudy has been successfully requested.":
            return jsonify({'msg': res}), 201
        return jsonify({'msg': res}), 201
