# -*- coding: utf-8 -*-
import json
import os

from flask import Flask, make_response, request, jsonify
from mailchimp3 import MailChimp


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        self.client = MailChimp(mc_api=os.getenv('MAILCHIMP_API_KEY'), mc_user=os.getenv('MAILCHIMP_USERNAME'))


    def add_to_list(self):
        req = request.get_json()
        listName = req['listName']
        userEmail = req['userEmail']
        list_id = self.get_list_id(listName)

        data = self.subscriber_data()
        # Add email to dict as it's a required attribute
        data.update({'email_address': userEmail})

        resp=self.client.lists.members.create(list_id, data)
        
        return self.end(resp)


    def delete_from_list(self):
        req = request.get_json()
        listName = req['listName']
        userEmail = req['userEmail']
        list_id = self.get_list_id(listName)
        user_id = self.get_user_id(list_id, userEmail)

        self.client.lists.members.delete(list_id, user_id)
        return jsonify( response={
                        'success': True,
                        'message': 'list deleted successfully'
                    },
                       status_code=200     )


    def add_tags(self):
        req = request.get_json()
        listName = req['listName']
        userEmail = req['userEmail']
        tags = req['tags'].split(',')
        list_id = self.get_list_id(listName)
        user_id = self.get_user_id(list_id, userEmail)

        data = {'tags': list(map(lambda tag: {'name': tag, 'status': 'active'}, tags))}

        self.client.lists.members.tags.update(list_id, user_id, data)
        return jsonify(response={
                        'success': True,
                        'message': 'Tag added successfully'
                    },
                       status_code=200,)


    def update_subscriber(self):
        req = request.get_json()
        listName = req['listName']
        userEmail = req['userEmail']
        list_id = self.get_list_id(listName)
        user_id = self.get_user_id(list_id, userEmail)

        data = self.subscriber_data()

        resp=self.client.lists.members.update(list_id, user_id, data)
        return self.end(resp)


    # Prepares and returns subscriber's data as a dictionary
    def subscriber_data(self):
        req = request.get_json()
        data = {}
        merge_field_data = {}

        key_map = {
          'status': 'status',
          'firstName': 'FNAME',
          'lastName': 'LNAME',
          'newEmail': 'email_address',
          'address': 'ADDRESS',
          'phone': 'PHONE'
        }
        merge_field_exclusive = ['firstName', 'lastName', 'address', 'phone']

        for key, val in req.items():
            if key != 'listName' and key != 'userEmail':
                if key in merge_field_exclusive:
                    merge_field_data.update({key_map[key]: val})
                else:
                    data.update({key_map[key]: val})

        data.update({'merge_fields': merge_field_data})
        return data


    # Returns List ID from List name input
    def get_list_id(self, listName):
        listName = listName
        for x in self.client.lists.all(get_all=True, fields="lists.name,lists.id")['lists']:
            if(x['name'] == listName):
                return x['id']

        raise Exception("Invalid list name: MailChimp list name '%s' not found." % listName)


    # Returns User ID (Subscriber's Hash)
    def get_user_id(self, list_id, userEmail):
        list_id = list_id
        userEmail = userEmail
        for x in self.client.lists.members.all(list_id, get_all=True, \
          fields="members.email_address,members.id")['members']:
            if (x['email_address'] == userEmail):
                return x['id']

        raise Exception("Invalid user email: User not found.")
        
    # Returns json response
    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    @staticmethod
    def app_error(e):
        return json.dumps({'message': str(e)}), 400


if __name__ == '__main__':
    for env_var in ["MAILCHIMP_API_KEY", "MAILCHIMP_USERNAME"]:
        assert env_var in os.environ, \
            f"The environment variable '{env_var}' must be set."

    handler = Handler()
    handler.app.register_error_handler(Exception, handler.app_error)
    handler.app.add_url_rule('/subscribers/add', 'add', handler.add_to_list, methods=['post'])
    handler.app.add_url_rule('/subscribers/delete', 'delete', handler.delete_from_list, methods=['post'])
    handler.app.add_url_rule('/tags', 'addtag', handler.add_tags, methods=['post'])
    handler.app.add_url_rule('/subscribers/updatesubscriber', 'updatesubscriber', handler.update_subscriber, \
    methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
