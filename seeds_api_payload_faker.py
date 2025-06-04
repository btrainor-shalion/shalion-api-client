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


    seed_type = payload.get("attributes", {}).get("type", None)
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
            "keywordType": random.choice(["CATEGORY", "BRANDED"]),
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


def fake_job(partial={}, environment="develop"):

    payload = {
        "name": f"QA job {random.randint(1000, 9999)}",
        "destinationJobId": None,
        "metadata": {
            faker.Faker().word(): faker.Faker().word(),
            faker.Faker().word(): faker.Faker().word()
        },
        "extractionConfig": {
            "extractionType": random.choice(["SEARCH", "SHELF", "AD", "DIGITAL_SHELF_PLP", "DIGITAL_SHELF_PDP", "MEDIA"]),
        }
    }

    response = requests.get(build_url("store-packages", environment=environment))

    store_package = random.choice(response.json())
    store_package_id = store_package["id"]
    payload["storePackageId"] = store_package_id

    store_package_geoloc_mode = store_package["geolocMode"]
    if store_package_geoloc_mode == "AUTOMATIC":
        payload["geolocMode"] = "AUTOMATIC"
    else:
        payload["geolocMode"] = "MANUAL"


    if payload["extractionConfig"]["extractionType"] in ["SEARCH", "SHELF", "DIGITAL_SHELF_PLP", "MEDIA"]:
        payload["extractionConfig"]["maxPages"] = random.randint(1, 10)
        payload["extractionConfig"]["maxRank"] = random.randint(1, 100)

    elif payload["extractionConfig"]["extractionType"] == "DIGITAL_SHELF_PDP":
        payload["extractionConfig"]["hasToExtractMarketplace"] = random.choice([True, False])
        payload["extractionConfig"]["hasToExtractReviews"] = random.choice([True, False])



    # Override or add new payload keys
    payload.update(partial)

    return payload
