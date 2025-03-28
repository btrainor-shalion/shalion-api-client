import re
import urllib.parse


api_paths = {
    "ecometry-tasks": [
        "/v1.0/admin/box-jobs",
        "/v1.0/admin/box-seed-timeframes",
        "/v1.0/admin/boxes",
        "/v1.0/admin/discovery/seeds",
        "/v1.0/admin/extraction-types",
        "/v1.0/admin/job-locations",
        "/v1.0/admin/job-seeds",
        "/v1.0/admin/job-timeframes",
        "/v1.0/admin/jobs",
        "/v1.0/admin/project-jobs",
        "/v1.0/admin/projects",
        "/v1.0/admin/seeds",
        "/v1.0/admin/timeframes"
    ],
    "orders-management": [
        "/v2.0/orders",
        "/v2.0/executions",
        "/v2.0/error-indicators",
        "/v2.0/machine-sizes",
        "/v2.0/delivery-methods"
    ]
}


def build_url(resource, environment="develop", resource_id=None, 
              related_resource=None, filters={}):

    scheme = "https://"

    domain = build_domain(resource, environment)
    path = build_path(resource, resource_id, related_resource)

    filter_string = ""
    if len(filters) > 0:
        filter_string = "?" + urllib.parse.urlencode(filters)

    return f"{scheme}{domain}{path}{filter_string}"


def build_domain(resource, environment="develop"):

    environment_subdomains = {
        "prod": "v2",
        "staging": "ondemand",
        "develop": "develop"
    }

    for api in api_paths:
        for path in api_paths[api]:
            if re.search(r"/{resource}$".format(resource=resource), path):
                return f"{api}-api-{environment}.{environment_subdomains[environment]}.shalion.com"

    raise ValueError("Resource not found in API paths.")


def build_path(resource, resource_id=None, related_resource=None):

    for api in api_paths:
        for path in api_paths[api]:
            if re.search(r"/{resource}$".format(resource=resource), path):
                if resource_id is not None and related_resource is not None:
                    return f"{path}/{resource_id}/{related_resource}"
                elif resource_id is not None:
                    return f"{path}/{resource_id}"

                return path

    raise ValueError("Resource not found in API paths.")