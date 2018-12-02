import requests
import json
from requests_oauthlib import OAuth1Session
from requests.auth import HTTPBasicAuth
def send_delete_request(request_url):
    r = requests.delete(url=request_url)
    return r
def send_delete_request_with_Auth1(request_url,client_key, client_secret, resource_owner_key,resource_owner_secret):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.delete(request_url)
    data = json.loads(r.content)
    return data
def send_get_request_with_Auth(request_url, user_name, password):
    r = requests.get(request_url, auth=HTTPBasicAuth(user_name, password))
    data = json.loads(r.content)
    return data