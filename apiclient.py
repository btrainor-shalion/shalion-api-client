import random
import requests
from urllib.parse import urlencode

import request_url_builder
import seeds_api_payload_faker


def create_seed(partial={}, environment="develop"):

    url = request_url_builder.build_url("seeds", environment)
    payload = seeds_api_payload_faker.fake_seed(partial, environment)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def get_seed(filters={}, environment="develop"):

    url = request_url_builder.build_url("seeds", environment)
    url += "?" + urlencode(filters)

    headers = {"accept": "application/json", "Content-Type": "application/json"}
    
    response = requests.get(url, headers=headers)

    return random.choice(response.json())


def create_job(partial={}, environment="develop"):

    url = request_url_builder.build_url("jobs", environment)
    print(url)
    payload = seeds_api_payload_faker.fake_job(partial, environment)
    print(payload)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response