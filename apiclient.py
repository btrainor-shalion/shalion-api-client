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
    seeds = response.json()
    if len(seeds) == 0:
        return None
    else:
        return random.choice(seeds)


def create_job(partial={}, environment="develop"):

    url = request_url_builder.build_url("jobs", environment)
    payload = seeds_api_payload_faker.fake_job(partial, environment)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_store_package(partial={}, environment="develop"):

    url = request_url_builder.build_url("store-packages", environment)
    print(url)
    payload = seeds_api_payload_faker.fake_store_package(partial, environment)
    print(json.dumps(payload))
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response

def add_store_package_seed(store_package_id, environment="develop"):

    store_package_url = request_url_builder.build_url("store-packages", environment, filters={"ids": store_package_id})
    store_package_response = requests.get(store_package_url)
    store_package = store_package_response.json()[0]

    store_package_boxes_url = request_url_builder.build_url("store-packages", environment=environment, resource_id=store_package_id, related_resource="boxes")

    store_package_boxes = requests.get(store_package_boxes_url).json()
    store_package_box = random.choice(store_package_boxes)

    seed = get_seed(filters={"store_ids": store_package["store"]["id"]}, environment=environment)
    timeframe = get_timeframe(environment=environment)

    box_url = request_url_builder.build_url("boxes", environment, resource_id=store_package_box["id"], related_resource="entries")
    payload = {
        "entries": [
            {
                "seedId": seed["id"],
                "timeframeId": timeframe["id"],
                "isForDiscovery": random.choice([True, False])
            }
        ]
    }

    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = requests.post(box_url, json=payload, headers=headers)

    return response

def create_retailer_package(partial={}, environment="develop"):

    url = request_url_builder.build_url("retailer-packages", environment)
    payload = seeds_api_payload_faker.fake_retailer_package(partial, environment)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_tag(partial={}, environment="develop"):

    url = request_url_builder.build_url("tags", environment)
    print(url)
    payload = seeds_api_payload_faker.fake_tag(partial, environment)
    print(payload)
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_seed_subscriptions(partial={}, environment="develop"):

    url = request_url_builder.build_url("seed-subscriptions", environment)
    print(url)
    payload = seeds_api_payload_faker.fake_seed_subscriptions(partial, environment)
    print(json.dumps(payload))
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_box_subscriptions(partial={}, environment="develop"):

    url = request_url_builder.build_url("box-subscriptions", environment)
    print(url)
    payload = seeds_api_payload_faker.fake_box_subscriptions(partial, environment)
    print(json.dumps(payload))
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def create_location(partial={}, environment="develop"):

    url = request_url_builder.build_url("locations", environment)
    print(url)
    payload = seeds_api_payload_faker.fake_location(partial, environment)
    print(json.dumps(payload))
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response


def get_timeframe(filters={}, environment="develop"):

    url = request_url_builder.build_url("timeframes", environment)
    url += "?" + urlencode(filters)

    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    return random.choice(response.json())