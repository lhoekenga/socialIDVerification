from django.test import SimpleTestCase
from django.urls import reverse

from ..views import scrub_ssn

import datetime
import logging

class ViewTests(SimpleTestCase):
    """
    Test all views
    """

    # Setup all needed forms and disable logging
    def setUp(self):
        self.test_valid_form_data = {
            'first_name': 'mega',
            'last_name': 'man',
            'birth_date': datetime.date(2000, 1, 1),
            'degree_year': '2008',
            'umid': '12345678',
        }
        self.test_invalid_form_data = {
            'first_name': 'mega',
            'last_name': 'man1',
            'birth_date': datetime.date(2000, 1, 1),
            'degree_year': '2008',
            'umid': '12345678',
        }
        self.test_ssn_form_data = {
            'first_name': 'mega',
            'last_name': 'man1',
            'birth_date': datetime.date(2000, 1, 1),
            'degree_year': '2008',
            'ssn': '1234',
        }
        logging.disable(logging.CRITICAL)

    # Reenable logging
    def tearDown(self):
        logging.disable(logging.NOTSET)

    # Test we can GET the page
    def test_get_verify(self):
        response = self.client.get(reverse('verify'))
        self.assertEqual(response.status_code, 200)

    # Test we raise the correct error on an empty post
    def test_empty_post_verify(self):
        response = self.client.post(reverse('verify'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Unable to validate identity', str(response.content))
        self.assertIn('<VerifyForm bound=True, valid=False, fields=(first_name;last_name;birth_date;degree_year;umid;lookupID;ssn)>', str(response.context))

    # Test we raise the correct error on invalid data
    def test_invalid_post_verify(self):
        response = self.client.post(reverse('verify'), self.test_invalid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Unable to validate identity', str(response.content))

    # We can't test valid data because we don't want to store it
    def test_valid_post_verify(self):
        response = self.client.post(reverse('verify'), self.test_valid_form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/verify/confirmed/')

    # For logging purposes, make sure SSN gets scrubbed properly
    def test_scrub_ssn(self):
        cleaned_form = scrub_ssn(self.test_ssn_form_data)
        self.assertEqual('xxxx', cleaned_form['ssn'])
        self.assertNotEqual('1324', cleaned_form['ssn'])

