import unittest
import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth {}'.format('AQAAAABdP1gCAADLWzET0A8pA0Xvps5aFVoeNjM')
}
params = {'path': 'new_folder/'}
ya_url = 'https://cloud-api.yandex.net/v1/disk/resources'

class TestRequests(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_req(self):
        result = requests.put(ya_url, headers=headers, params=params)
        self.assertEqual(result.status_code, 201)

