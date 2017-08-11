from django.test import SimpleTestCase

from ..forms import VerifyForm

import datetime

# Create your tests here.

class VerifyFormTests(SimpleTestCase):
    """
    Test valid and invalid form data
    """

    # Test that form validates
    def test_valid_data(self):
        form = VerifyForm({
            'first_name': 'mega',
            'last_name': 'man',
            'birth_date': datetime.date(2000, 1, 1),
            'degree_year': '2008',
            'verifyidRadios': 'umid',
            'umid': '12345678',
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['first_name'], 'mega')
        self.assertEqual(form.cleaned_data['last_name'], 'man')
        self.assertEqual(form.cleaned_data['birth_date'], datetime.date(2000, 1, 1))
        self.assertEqual(form.cleaned_data['degree_year'], '2008')
        self.assertEqual(form.cleaned_data['verifyidRadios'], 'umid')
        self.assertEqual(form.cleaned_data['umid'], '12345678')

    # Test for all required fields
    def test_blank_data(self):
        form = VerifyForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
        self.assertEqual(form.errors['last_name'], ['This field is required.'])
        self.assertEqual(form.errors['birth_date'], ['This field is required.'])
        self.assertEqual(form.errors['degree_year'], ['This field is required.'])
        self.assertEqual(form.errors['verifyidRadios'], ['This field is required.'])

    # Test leading and trailing zeros are not stripped
    def test_zero_trimming_data(self):
        test_ssn = '0110'
        form = VerifyForm({
            'first_name': 'mega',
            'last_name': 'man',
            'birth_date': datetime.date(2000, 1, 1),
            'degree_year': '2008',
            'verifyidRadios': 'ssn',
            'ssn': test_ssn,
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['ssn'], test_ssn)
