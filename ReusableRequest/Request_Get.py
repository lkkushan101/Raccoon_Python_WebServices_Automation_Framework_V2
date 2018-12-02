import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
import json
def send_get_request(request_url):
    r = requests.get(request_url)
    data = json.loads(r.content)
    return data
def send_get_request_with_Auth(request_url, user_name, password):
    r = requests.get(request_url, auth=HTTPBasicAuth(user_name, password))
    data = json.loads(r.content)
    return data
def send_get_request_with_Auth1(request_url,client_key, client_secret, resource_owner_key,resource_owner_secret):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.get(url)
    data = json.loads(r.content)
    return data