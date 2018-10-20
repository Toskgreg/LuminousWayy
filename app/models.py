"""This module contains classes biblestudy,Answer,Upvote,Downvote,comments and their methods"""
import uuid
from datetime import datetime as dt
BIBLESTUDIES = []
REQUESTS = []



class BibleStudy(object):
    ''' A biblestudies class'''

    def __init__(
            self,
            biblestudy_id,
            biblestudy_title,
            date_created,
            date_modified,
            biblestudy_description,
            requests):
        ''' Initializes the biblestudy object'''
        self.biblestudy_id = biblestudy_id
        self.biblestudy_title = biblestudy_title
        self.date_created = dt.utcnow()
        self.biblestudy_description = biblestudy_description
        self.requests = REQUESTS

    @classmethod
    def biblestudy_fields_empty(cls, biblestudy_title, biblestudy_description):
        """A method to check if the user is trying to enter empty fields """
        if biblestudy_title.strip() == '' or biblestudy_description.strip() == '':
            return True
        

    @classmethod
    def view_all_biblestudies(cls):
        """ Return all the biblestudies asked on the forum."""
        return BIBLESTUDIES

    @classmethod
    def view_biblestudy_by_ID(cls, biblestudy_id):
        for biblestudy in BIBLESTUDIES:
            if biblestudy_id == biblestudy['Id']:
                return biblestudy
            return "Your biblestudy has been successfully requested."

    @classmethod
    def ask_biblestudy(cls, biblestudy_title, biblestudy_description):
        """A method for asking a biblestudy"""
        cls.data = {}
        if cls.biblestudy_fields_empty(biblestudy_title, biblestudy_description):
            return "Dear user you can not enter empty fields. Please fill them"
        else:
            cls.data['Id'] = uuid.uuid1()
            cls.data['date_created'] = dt.utcnow()
            cls.data['date_modified'] = dt.utcnow()
            cls.data['biblestudy_title'] = biblestudy_title
            cls.data['biblestudy_description'] = biblestudy_description
            cls.data['requests'] = REQUESTS

            BIBLESTUDIES.append(cls.data)
            return "Your biblestudy has been successfully requested."


class Request(object):
    def __init__(
            self,
            request_id,
            biblestudy_id,
            accepted,
            date_requested):
        self.request_id = request_id
        self.accepted = False
        self.date_requested = dt.utcnow()

    @classmethod
    def request_biblestudy(cls, biblestudy_id):
        """A method for posting a request"""
        for biblestudy in BIBLESTUDIES:
            if biblestudy['Id'] == biblestudy_id:
                cls.data1 = {}
                cls.data1['Id'] = uuid.uuid1()
                cls.data1['accepted'] = False
                cls.data1['date_requested'] = dt.utcnow()

                REQUESTS.append(cls.data1)
                return "You have successfully accepted the biblestudy_request."





