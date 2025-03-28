import unittest
from seeds_api_payload_faker import fake_seed, fake_tag


class TestFakeSeed(unittest.TestCase):

    def test_fake_seed_empty(self):

        seed = fake_seed()

        self.assertIsInstance(seed, dict)
        self.assertIn("description", seed)
        self.assertIn("isQaCandidate", seed)
        self.assertIn("storeId", seed)
        self.assertIn("categoryId", seed)


    def test_fake_seed_type_url(self):

        seed = fake_seed({"attributes": {"type": "URL"}})

        self.assertIsInstance(seed, dict)
        self.assertIn("description", seed)
        self.assertIn("isQaCandidate", seed)
        self.assertIn("storeId", seed)
        self.assertIn("categoryId", seed)

        self.assertIn("isFromDiscovery", seed["attributes"])
        self.assertIn("url", seed["attributes"])
        self.assertIn("pageType", seed["attributes"])
        self.assertIn("discoveryKey", seed["attributes"])
        self.assertIn("type", seed["attributes"])
        self.assertEqual(seed["attributes"]["type"], "URL")


    def test_fake_seed_type_api(self):

        seed = fake_seed({"attributes": {"type": "API"}})

        self.assertIsInstance(seed, dict)
        self.assertIn("description", seed)
        self.assertIn("isQaCandidate", seed)
        self.assertIn("storeId", seed)
        self.assertIn("categoryId", seed)

        self.assertIn("isFromDiscovery", seed["attributes"])
        self.assertIn("apiOrigin", seed["attributes"])
        self.assertIn("pageType", seed["attributes"])
        self.assertIn("discoveryKey", seed["attributes"])
        self.assertIn("type", seed["attributes"])
        self.assertEqual(seed["attributes"]["type"], "API")


    def test_fake_seed_type_keyword(self):

        seed = fake_seed({"attributes": {"type": "KEYWORD"}})

        self.assertIsInstance(seed, dict)
        self.assertIn("description", seed)
        self.assertIn("isQaCandidate", seed)
        self.assertIn("storeId", seed)
        self.assertIn("categoryId", seed)

        self.assertIn("isFromDiscovery", seed["attributes"])
        self.assertIn("keyword", seed["attributes"])
        self.assertIn("keywordType", seed["attributes"])
        self.assertIn("type", seed["attributes"])
        self.assertEqual(seed["attributes"]["type"], "KEYWORD")


    def test_fake_seed_with_store(self):
        
        fake_store_id = "f58d0c21-6195-4a6f-82df-7f577192707a"
        seed = fake_seed({"storeId": fake_store_id})

        self.assertIsInstance(seed, dict)
        self.assertIn("description", seed)
        self.assertIn("isQaCandidate", seed)
        self.assertIn("storeId", seed)
        self.assertEqual(seed["storeId"], fake_store_id)
        self.assertIn("categoryId", seed)



class TestFakeTag(unittest.TestCase):

    def test_fake_tag_empty(self):

        tag = fake_tag()

        self.assertIsInstance(tag, dict)
        self.assertIn("name", tag)
        self.assertIn("clientId", tag)
        self.assertIn("parentId", tag)


    def test_fake_tag_with_client(self):
        
        fake_client_id = "f58d0c21-6195-4a6f-82df-7f577192707a"
        tag = fake_tag({"clientId": fake_client_id})

        self.assertIsInstance(tag, dict)
        self.assertIn("name", tag)
        self.assertIn("clientId", tag)
        self.assertIn("parentId", tag)

    def test_fake_tag_with_parent(self):
        
        fake_parent_id = "d41a52cd-ffce-4f54-b990-75623e57b49c"
        tag = fake_tag({"parentId": fake_parent_id})

        self.assertIsInstance(tag, dict)
        self.assertIn("name", tag)
        self.assertIn("clientId", tag)
        self.assertIn("parentId", tag)


if __name__ == '__main__':
    unittest.main()