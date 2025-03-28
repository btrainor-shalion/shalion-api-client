import requests
import random
import faker
from request_url_builder import build_url


def fake_seed(partial={}, environment="develop"):

    payload = {
        "description": "string",
        "isQaCandidate": random.choice([True, False]),
    }

    # Override or add new payload keys
    payload.update(partial)

    if "categoryId" not in payload:
        response = requests.get(build_url("categories", environment=environment))
        category_id = random.choice(response.json())["id"]
        payload["categoryId"] = category_id

    if "storeId" not in payload:
        response = requests.get(build_url("stores", environment=environment))
        store_id = random.choice(response.json())["id"]
        payload["storeId"] = store_id


    seed_type = payload.get("attributes", {}).get("type", {})
    if seed_type is None:
        seed_type = random.choice(["URL", "API", "KEYWORD"])

    if seed_type == "URL":
        payload["attributes"] = {
            "pageType": random.choice(["HOME", "CATEGORY", "SUBCATEGORY", "OFFERS"]),
            "discoveryKey": faker.Faker().word(),
            "isFromDiscovery": random.choice([True, False]),
            "url": faker.Faker().url(),
            "type": seed_type
        }

    elif seed_type == "API":
        payload["attributes"] = {
            "pageType": random.choice(["HOME", "CATEGORY", "SUBCATEGORY", "OFFERS"]),
            "discoveryKey": faker.Faker().word(),
            "isFromDiscovery": random.choice([True, False]),
            "apiOrigin": {
                "additionalProp1": {},
                "additionalProp2": {},
                "additionalProp3": {}
            },
            "type": seed_type
        }

    elif seed_type == "KEYWORD":
        payload["attributes"] = {
            "keywordType": random.choice(["HOME", "CATEGORY", "SUBCATEGORY", "OFFERS"]),
            "discoveryKey": faker.Faker().word(),
            "isFromDiscovery": random.choice([True, False]),
            "keyword": faker.Faker().word(),
            "type": seed_type
        }



    return payload


def fake_tag(partial={}, environment="develop"):
    
    payload = {
        "name": f"QA tag {faker.Faker().word()}",
        "parentId": None
    }

    # Override or add new payload keys
    payload.update(partial)

    if "clientId" not in payload:
        response = requests.get(build_url("clients", environment=environment))
        client_id = random.choice(response.json())["id"]
        payload["clientId"] = client_id

    has_parent = random.choice([True, False])
    if has_parent:
        response = requests.get(build_url("tags", environment=environment))
        parent_id = random.choice(response.json())["id"]
        payload["parentId"] = parent_id


    return payload


def fake_job(partial):
    pass
