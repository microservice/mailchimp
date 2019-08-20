import pytest
from flask import Flask

@pytest.fixture(scope='module')
def app() -> Flask:
    from app import Handler
    handler = Handler()
    handler.app.add_url_rule('/subscribers/add', 'add', handler.add_to_list, methods=['post'])
    handler.app.add_url_rule('/subscribers/delete', 'delete', handler.delete_from_list, methods=['post'])
    handler.app.add_url_rule('/tags', 'addtag', handler.add_tags, methods=['post'])
    handler.app.add_url_rule('/subscribers/updatesubscriber', 'updatesubscriber', handler.update_subscriber, \
    methods=['post'])
     
    return handler.app
