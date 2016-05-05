import json
import requests
import threading
from hashlib import md5

from django.conf import settings

from libs.email import send_email


class ActionSet:
    EMPTY = 0
    CREATE = 1
    UPDATE = 2


def request(method, slug, data=None):
    return method(settings.MAILCHIMP_DATACENTER + slug, data=data,
                  auth=(settings.MAILCHIMP_USER, settings.MAILCHIMP_API_KEY))

def json_request(method, slug, data):
    return request(method, slug, json.dumps(data))

def get_list_slug():
    return 'lists/{}/'.format(settings.MAILCHIMP_ROOMIT_LIST_ID)

def get_user_id(email):
    return md5(email.lower()).hexdigest()

def check_user_status(user_id):
    response = request(requests.get, '{}/members/{}'.format(get_list_slug(), user_id))
    if response.status_code == 404:
        return ActionSet.CREATE

    if response.json()['status'] != settings.MAILCHIMP_SUBSCRIBED:
        return ActionSet.UPDATE

    return ActionSet.EMPTY

def create_user(email):
    response = json_request(requests.post, '{}/members/'.format(get_list_slug()), {
        'email_address': email,
        'status': settings.MAILCHIMP_SUBSCRIBED
    })

    return response.status_code == 200

def update_user(user_id):
    response = json_request(requests.patch, '{}/members/{}'.format(get_list_slug(), user_id), {
        'status': settings.MAILCHIMP_SUBSCRIBED
    })

    return response.status_code == 200

def add_email_to_list(email):
    user_id = get_user_id(email)
    status = check_user_status(user_id)
    if status == ActionSet.CREATE:
        return create_user(email)

    if status == ActionSet.UPDATE:
        return update_user(user_id)

def validate_and_send_email(email):

    def validate_func():
        if add_email_to_list(email):
            send_email(settings.AFTER_SUBSCRIBE_TEMPLATE, email)

    threading.Thread(target=validate_func).start()

