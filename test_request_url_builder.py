import unittest
from request_url_builder import build_path, build_domain, build_url


class TestURLBuilder(unittest.TestCase):

    def test_build_domain_default(self):
        self.assertEqual(build_domain("timeframes"),  "ecometry-tasks-api-develop.develop.shalion.com")

    def test_build_domain_staging(self):
        self.assertEqual(build_domain("timeframes", "staging"),  "ecometry-tasks-api-staging.ondemand.shalion.com")

    def test_build_domain_prod(self):
        self.assertEqual(build_domain("timeframes", "prod"),  "ecometry-tasks-api-prod.v2.shalion.com")

    def test_build_path_timeframes(self):
        self.assertEqual(build_path("timeframes"), "/v1.0/admin/timeframes")

    def test_build_path_boxes(self):
        self.assertEqual(build_path("boxes"), "/v1.0/admin/boxes")

    def test_build_path_orders(self):
        self.assertEqual(build_path("orders"), "/v2.0/orders")


    def test_build_url_default(self):
        self.assertEqual(build_url("timeframes"), "https://ecometry-tasks-api-develop.develop.shalion.com/v1.0/admin/timeframes")

    def test_build_url_staging(self):
        self.assertEqual(build_url("timeframes", environment="staging"), "https://ecometry-tasks-api-staging.ondemand.shalion.com/v1.0/admin/timeframes")

    def test_build_url_prod(self):
        self.assertEqual(build_url("timeframes", environment="prod"), "https://ecometry-tasks-api-prod.v2.shalion.com/v1.0/admin/timeframes")

    def test_build_url_default_with_filters(self):
        self.assertEqual(build_url("timeframes", filters={"store_ids": "dc0ffa85-9069-442a-81d0-ff610ba9ad27"}), "https://ecometry-tasks-api-develop.develop.shalion.com/v1.0/admin/timeframes?store_ids=dc0ffa85-9069-442a-81d0-ff610ba9ad27")

    def test_build_url_default_with_resource_id(self):
        self.assertEqual(build_url("timeframes", resource_id="dc0ffa85-9069-442a-81d0-ff610ba9ad27"), "https://ecometry-tasks-api-develop.develop.shalion.com/v1.0/admin/timeframes/dc0ffa85-9069-442a-81d0-ff610ba9ad27")

    def test_build_url_default_with_resource_id_and_filters(self):
        self.assertEqual(build_url("timeframes", resource_id="dc0ffa85-9069-442a-81d0-ff610ba9ad27",
                                   filters={"store_ids": "f972c7cc-844d-489b-b80d-98bac3588420"}), "https://ecometry-tasks-api-develop.develop.shalion.com/v1.0/admin/timeframes/dc0ffa85-9069-442a-81d0-ff610ba9ad27?store_ids=f972c7cc-844d-489b-b80d-98bac3588420")


if __name__ == '__main__':
    unittest.main()