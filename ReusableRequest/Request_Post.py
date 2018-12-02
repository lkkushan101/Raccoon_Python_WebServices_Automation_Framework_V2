import requests
import json
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
def send_post_request(request_url,request_parameters):
    r = requests.post(url=request_url, data = request_parameters)
    return r
def send_get_request_with_Auth(request_url,request_parameters, user_name, password):
    r = requests.post(request_url, request_parameters, auth=HTTPBasicAuth(user_name, password))
    data = json.loads(r.content)
    return data
def send_post_request_with_Auth1(request_url,request_parameters,client_key, client_secret, resource_owner_key,resource_owner_secret):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.post(request_url, data=request_parameters)
    data = json.loads(r.content)
    return data