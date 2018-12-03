import requests
import json
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
def send_post_request_with_header(request_url,request_parameters, header):
    r = requests.post(url=request_url, data=request_parameters, header={header})
    return r
def send_get_request_with_Auth_with_header(request_url,request_parameters, user_name, password,header):
    r = requests.post(request_url, request_parameters, auth=HTTPBasicAuth(user_name, password), header={header})
    data = json.loads(r.content)
    return data
def send_post_request_with_Auth1_with_header(request_url,request_parameters,client_key, client_secret, resource_owner_key,resource_owner_secret,header):
    authentication = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
    r = authentication.post(request_url, data=request_parameters, header={header})
    data = json.loads(r.content)
    return data