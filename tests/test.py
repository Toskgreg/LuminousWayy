from run import app
import unittest
from flask import json


class TestRequest(unittest.TestCase):
    def setUp(self):
        """This instanciates the flask app for a background no-live-server operations for testing purposes"""
        self.app = app.test_client()

    def test_biblestudy_creation(self):
        """Test API can create a biblestudy (POST request)"""
        response = self.app.post('api/v1/biblestudies/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "biblestudy_title": "What is an API ?",
                                     "biblestudy_description": " in detail what an API is?"
                                 }))

        self.assertEqual(response.status_code, 201)

    def test__fields_are_empty(self):
        """Test if a biblestudy can be created without data"""
        response = self.app.post('api/v1/biblestudies/',
                                    content_type='application/json',
                                    data=json.dumps({
                                        "biblestudy_title":"",
                                        "biblestudy_description":""
                                    }))

        self.assertIn("Dear user you can not enter empty fields. Please fill them",
                      str(response.data))

    def test_return_created_code_if_request_is_valid(self):
        """This method checks if a valid request has been posted and returns an apropriate status code 201"""
        # post data
        response = self.app.post('api/v1/biblestudies/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "biblestudy_title": "What is an API ?",
                                     "biblestudy_description": " in detail what an API is?"
                                 }))

        self.assertEqual(response.status_code, 201)

        response = self.app.get('api/v1/biblestudies/')
        self.assertEqual(response.status_code, 200)

        results = json.loads(response.data.decode())

        for biblestudy in results:
            response = self.app.post('api/v1/biblestudies/{}/request/'
                                     .format(biblestudy['Id']),
                                     content_type='application/json',
                                   )
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                "You have successfully accepted the biblestudy_request.",
                str(response.data))
            response = self.app.get(
                'api/v1/biblestudies/{}'.format(biblestudy['Id']))
            self.assertEqual(response.status_code, 200)


    def test_api_can_view_all_biblestudies(self):
        """Test BIBLESTUDYAPI can view all (GET request)."""
        response = self.app.post('api/v1/biblestudies/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "biblestudy_title": "What is an API ?",
                                     "biblestudy_description": " in detail what an API is?"
                                 }))

        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/biblestudies/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", str(response.data))

    def test_api_can_get_biblestudy_by_id(self):
        """Test API can fetch a single biblestudy by using it's id."""
        # post data
        response = self.app.post('api/v1/biblestudies/',
                                 content_type='application/json',
                                 data=json.dumps({
                                     "biblestudy_title": "What is an API ?",
                                     "biblestudy_description": " in detail what an API is?"
                                 }))
        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/biblestudies/')
        self.assertEqual(response.status_code, 200)

        results = json.loads(response.data.decode())
        for biblestudy in results:
            result = self.app.get(
                'api/v1/biblestudies/{}'.format(biblestudy['Id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(biblestudy['Id'], str(result.data))
