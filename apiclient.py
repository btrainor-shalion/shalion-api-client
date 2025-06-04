import random
import requests
import json
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
    payload = seeds_api_payload_faker.fake_job(partial, environment)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_store_package(partial={}, environment="develop"):

    url = request_url_builder.build_url("store-packages", environment)
    payload = seeds_api_payload_faker.fake_store_package(partial, environment)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_retailer_package(partial={}, environment="develop"):

    url = request_url_builder.build_url("retailer-packages", environment)
    payload = seeds_api_payload_faker.fake_retailer_package(partial, environment)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response