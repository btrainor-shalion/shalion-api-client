import requests
import random
import faker
from request_url_builder import build_url
from datetime import timedelta


def fake_seed(partial={}, environment="develop"):

    payload = {
        "description": f"QA random seed {random.randint(1000, 9999)}",
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
        "name": f"QA tag {random.randint(1000, 9999)}",
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


def fake_store_package(partial={}, environment="develop"):

    payload = {
        "name": f"QA store package {random.randint(10000, 99999)}",
        "locationsConfig": {
            "geolocMode": None
        },
        "isAdHoc": random.choice([True, False]),
        "retailerPackageId": None,
        "storeId": None,
        "boxIds": [],
        "locationIds": []
    }

    # Override or add new payload keys
    payload.update(partial)

    if payload["retailerPackageId"] is None:
        retailer_packages_response = requests.get(build_url("retailer-packages", environment=environment))
        retailer_package = random.choice(retailer_packages_response.json())
        payload["retailerPackageId"] = retailer_package["id"]

        stores_response = requests.get(build_url("stores", environment=environment,
                                          filters={"retailer_ids": retailer_package["retailer"]["id"]}))

        store = random.choice(stores_response.json())
        payload["storeId"] = store["id"]

        if store["storeType"] == "GEOLOC":
            payload["locationsConfig"]["geolocMode"] = "MANUAL"
        elif store["storeType"] == "FLAGSHIP":
            payload["locationsConfig"]["geolocMode"] = random.choice(["AUTOMATIC", "NO_GEOLOC"])


    if payload["boxIds"] == []:
        response = requests.get(build_url("boxes", environment=environment))
        boxes = response.json()
        if boxes:
            payload["boxIds"] = random.sample([box["id"] for box in boxes], k=random.randint(1, len(boxes)))

    if payload["locationIds"] == []:
        response = requests.get(build_url("locations", environment=environment, filters={"store_id": payload["storeId"]}))
        locations = response.json()
        if locations:
            payload["locationIds"] = random.sample([location["id"] for location in locations], k=random.randint(1, len(locations)))


    return payload


def fake_retailer_package(partial={}, environment="develop"):

    payload = {
        "name": f"QA retailer package {random.randint(10000, 99999)}",
        "retailerId": None,
    }

    # Override or add new payload keys
    payload.update(partial)

    if payload["retailerId"] is None:
        response = requests.get(build_url("retailers", environment=environment))
        retailer = random.choice(response.json())
        payload["retailerId"] = retailer["id"]

    return payload


def fake_tag(partial={}, environment="develop"):

    payload = {
        "name": f"QA tag {random.randint(1000, 9999)}",
        "parentId": None,
        "clientId": None
    }

    # Override or add new payload keys
    payload.update(partial)

    if payload["clientId"] not in payload:
        response = requests.get(build_url("clients", environment=environment))
        client_id = random.choice(response.json())["id"]
        payload["clientId"] = client_id

    has_parent = random.choice([True, False])
    print("Has parent:", has_parent)
    if has_parent:
        response = requests.get(build_url("tags", environment=environment))
        parent_id = random.choice(response.json())["id"]
        payload["parentId"] = parent_id

    return payload


def fake_seed_subscriptions(partial={}, environment="develop"):

    payload = {
        "clientId": None,
        "storePackageId": None,
        "seedIds": [],
        "isForDiscovery": random.choice([True, False]),
        "validity": {
            "dateFrom": None,
            "dateTo": None
        }
    }

    # Override or add new payload keys
    payload.update(partial)

    if payload["clientId"] is None:
        response = requests.get(build_url("clients", environment=environment))
        client = random.choice(response.json())
        payload["clientId"] = client["id"]

    if payload["storePackageId"] is None:
        response = requests.get(build_url("store-packages", environment=environment))
        storePackage = random.choice(response.json())
        payload["storePackageId"] = storePackage["id"]

    if payload["seedIds"] == []:
        response = requests.get(build_url("seeds", environment=environment, filters={"store_package_ids": payload["storePackageId"]}))
        seeds = response.json()
        if seeds:
            payload["seedIds"] = random.sample([seed["id"] for seed in seeds], k=random.randint(1, len(seeds)))

    if payload["validity"]["dateFrom"] is None:
        payload["validity"]["dateFrom"] = faker.Faker().date_time_this_year()
        payload["validity"]["dateTo"] = payload["validity"]["dateFrom"] + timedelta(days=random.randint(1, 30))
        payload["validity"]["dateFrom"] = payload["validity"]["dateFrom"].isoformat()[:-3] + "Z"
        payload["validity"]["dateTo"] = payload["validity"]["dateTo"].isoformat()[:-3] + "Z"


    return payload