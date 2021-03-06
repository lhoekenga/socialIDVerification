from django.test import SimpleTestCase

import jwt
import logging

from ..cirrus_jwt import generate_jwt

# Create your tests here.

class GenerateJWTTests(SimpleTestCase):
    """
    Create a JWT using fake data, and ensure that the header is as expected
    """

    # Define our fake entry and disable logging
    def setUp(self):
        self.entry = {
            'umichRegDisplayGivenName': 'mega',
            'umichRegDisplaySurname': 'man',
            'umichRegUid': 'megaman',
            'umichRegEntityID': '13371337',
            'umichDirectoryID': '999-999-13379999999999999-999',
            'umichOudDacId': '0011223344',
            'umichOudPrefEmailAddress': 'megaman@gmail.com',
        }
        logging.disable(logging.CRITICAL)

    # Renable logging
    def tearDown(self):
        logging.disable(logging.NOTSET)

    # Call the function we want to test with our fake data and ensure we get start of expected payload
    # TODO: find a better way to test we get the expected token back
    def test_create_jwt(self):
        encoded_jwt = generate_jwt(self.entry)
        self.assertIn('eyJ', str(encoded_jwt))

