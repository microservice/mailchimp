# -*- coding: utf-8 -*-
import json
import os
import sys

from flask import Flask, make_response, request
from mailchimp3 import MailChimp


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        self.client = MailChimp(mc_api=os.getenv('API_KEY'), mc_user=os.getenv('USERNAME'))

    def add_to_list(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        try:
            list_id = self.get_list_id(list_name)
        except:
            raise

        data = self.subscriber_data()
        # Add email to dict as it's required
        data.update({'email_address': user_email})

        try:
            self.client.lists.members.create(list_id, data)
            return self.end({})
        except:
            raise


    def delete_from_list(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        try:
            list_id = self.get_list_id(list_name)
        except:
            raise
        try:
            user_id = self.get_user_id(list_id, user_email)
        except:
            raise

        try:
            self.client.lists.members.delete(list_id, user_id)
            return self.end({})
        except:
            raise


    def add_tags(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        tags = req['tags'].split(',')
        tag_data = []
        for tag in tags:
            tag_data.append({'name': tag, 'status': 'active'})
        data = {'tags': tag_data}

        try:
            list_id = self.get_list_id(list_name)
        except:
            raise
        try:
            user_id = self.get_user_id(list_id, user_email)
        except:
            raise

        try:
            self.client.lists.members.tags.update(list_id, user_id, data)
            return self.end({})
        except:
            raise


    def update_subscriber(self):
        req = request.get_json()
        list_name = req['list_name']
        user_email = req['user_email']
        try:
            list_id = self.get_list_id(list_name)
        except:
            raise
        try:
            user_id = self.get_user_id(list_id, user_email)
        except:
            raise

        data = self.subscriber_data()

        try:
            self.client.lists.members.update(list_id, user_id, data)
            return self.end({})
        except Exception as e:
            raise


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
            if key != 'list_name' and key != 'user_email' and key not in merge_field_exclusive:
                data.update({key_map[key]: val})
            elif key != 'list_name' and key != 'user_email':
                merge_field_data.update({key_map[key]: val})

        data.update({'merge_fields': merge_field_data})
        return data


    # Returns List ID from List name input
    def get_list_id(self, list_name):
        found = False
        list_name = list_name
        for x in self.client.lists.all(get_all=True, fields="lists.name,lists.id")['lists']:
            if(x['name'] == list_name):
                found = True
                return x['id']

        if not found:
            raise Exception('Invalid list name.')


    # Returns User ID (Subscriber's Hash)
    def get_user_id(self, list_id, user_email):
        found = False
        list_id = list_id
        user_email = user_email
        for x in self.client.lists.members.all(list_id, get_all=True, \
          fields="members.email_address,members.id")['members']:
            if (x['email_address'] == user_email):
                found = True
                return x['id']

        if not found:
            raise Exception("Invalid user email: User not found.")


    def not_found_error(self, e):
        return json.dumps({"message": str(e)}), 404


    def mailchimp_error(self, e):
        if e.args:
          return json.dumps({'success': False, 'error_code': e.args[0]['status'], 'error': e.args[0]['detail']}), 400
        else:
          self.end({'success': False, 'message': 'Some error occoured, please check your inputs.'})


    # Returns json response
    @staticmethod
    def end(res):
        res = res
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    if os.getenv('API_KEY') is None:
        print('API Key not found')
        sys.exit(1)

    if os.getenv('USERNAME') is None:
        print('USERNAME not found')
        sys.exit(1)

    handler = Handler()
    handler.app.register_error_handler(Exception, handler.not_found_error)
    handler.app.add_url_rule('/subscribers/add', 'add', handler.add_to_list, methods=['post'])
    handler.app.add_url_rule('/subscribers/delete', 'delete', handler.delete_from_list, methods=['post'])
    handler.app.add_url_rule('/tags', 'addtag', handler.add_tags, methods=['post'])
    handler.app.add_url_rule('/subscribers/updatesubscriber', 'updatesubscriber', handler.update_subscriber, \
    methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
