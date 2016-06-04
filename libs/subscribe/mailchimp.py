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

def get_list_slug(list_id):
    return 'lists/{}/'.format(list_id)

def get_user_id(email):
    return md5(email.lower()).hexdigest()

def check_user_status(user_id, list_id):
    response = request(requests.get, '{}/members/{}'.format(get_list_slug(list_id), user_id))
    if response.status_code == 404:
        return ActionSet.CREATE

    if response.json()['status'] != settings.MAILCHIMP_SUBSCRIBED:
        return ActionSet.UPDATE

    return ActionSet.EMPTY

def create_user(email, list_id):
    response = json_request(requests.post, '{}/members/'.format(get_list_slug(list_id)), {
        'email_address': email,
        'status': settings.MAILCHIMP_SUBSCRIBED
    })

    return response.status_code == 200

def update_user(user_id, list_id):
    response = json_request(requests.patch, '{}/members/{}'.format(get_list_slug(list_id), user_id), {
        'status': settings.MAILCHIMP_SUBSCRIBED
    })

    return response.status_code == 200

def add_email_to_list(email, list_id):
    user_id = get_user_id(email)
    status = check_user_status(user_id, list_id)
    if status == ActionSet.CREATE:
        return create_user(email, list_id)

    if status == ActionSet.UPDATE:
        return update_user(user_id, list_id)

def validate_and_send_email(email, list_id):

    def validate_func():
        if add_email_to_list(email, list_id):
            send_email(settings.AFTER_SUBSCRIBE_TEMPLATE, email)

    threading.Thread(target=validate_func).start()
