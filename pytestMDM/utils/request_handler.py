# utils/request_handler.py

import requests


def send_request(xml_data, endpoint):
    headers = {'Content-Type': 'application/xml'}
    response = requests.put(endpoint, data=xml_data, headers=headers)
    return response
