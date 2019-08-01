# -*- coding: utf-8 -*-
import json
import os

from flask import Flask, make_response, request
from mailchimp3 import MailChimp


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        self.client = MailChimp(mc_api=os.getenv('MAILCHIMP_API_KEY'), mc_user=os.getenv('MAILCHIMP_USERNAME'))


    def add_to_list(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        list_id = self.get_list_id(list_name)

        data = self.subscriber_data()
        # Add email to dict as it's a required attribute
        data.update({'email_address': user_email})

        self.client.lists.members.create(list_id, data)
        return self.end({})


    def delete_from_list(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        list_id = self.get_list_id(list_name)
        user_id = self.get_user_id(list_id, user_email)

        self.client.lists.members.delete(list_id, user_id)
        return self.end({})


    def add_tags(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        tags = req['tags'].split(',')
        list_id = self.get_list_id(list_name)
        user_id = self.get_user_id(list_id, user_email)

        data = {'tags': list(map(lambda tag: {'name': tag, 'status': 'active'}, tags))}

        self.client.lists.members.tags.update(list_id, user_id, data)
        return self.end({})


    def update_subscriber(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        list_id = self.get_list_id(list_name)
        user_id = self.get_user_id(list_id, user_email)

        data = self.subscriber_data()

        self.client.lists.members.update(list_id, user_id, data)
        return self.end({})


    # Prepares and returns subscriber's data as a dictionary
    def subscriber_data(self):
        req = request.get_json()
        data = {}
        merge_field_data = {}

        key_map = {
          'status': 'status',
          'first_name': 'FNAME',
          'last_name': 'LNAME',
          'new_email': 'email_address',
          'address': 'ADDRESS',
          'phone': 'PHONE'
        }

        merge_field_exclusive = ['first_name', 'last_name', 'address', 'phone']

        for key, val in req.items():
            if key != 'list_name' and key != 'user_email':
                if key in merge_field_exclusive:
                    merge_field_data.update({key_map[key]: val})
                else:
                    data.update({key_map[key]: val})

        data.update({'merge_fields': merge_field_data})
        return data


    # Returns List ID from List name input
    def get_list_id(self, list_name):
        list_name = list_name
        for x in self.client.lists.all(get_all=True, fields="lists.name,lists.id")['lists']:
            if(x['name'] == list_name):
                return x['id']

        raise Exception("Invalid list name: MailChimp list name '%s' not found." % list_name)


    # Returns User ID (Subscriber's Hash)
    def get_user_id(self, list_id, user_email):
        list_id = list_id
        user_email = user_email
        for x in self.client.lists.members.all(list_id, get_all=True, \
          fields="members.email_address,members.id")['members']:
            if (x['email_address'] == user_email):
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
