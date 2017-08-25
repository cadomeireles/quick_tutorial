import unittest

from pyramid import testing
from tutorial import hello_world


class TutorialViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        request = testing.DummyRequest()
        response = hello_world(request)

        self.assertEqual(response.status_code, 200)
