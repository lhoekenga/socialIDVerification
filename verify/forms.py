from django import forms
from django.core.validators import RegexValidator

# our new form
class VerifyForm(forms.Form):

    first_name = forms.CharField(
        required=True,
    )

    last_name = forms.CharField(
        required=True,
    )

    birth_date = forms.DateField(
        required=True,
    )

    degree_year = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^\d{4,4}$', 'Enter a valid four digit year')],
    )

    verifyidRadios = forms.CharField(
        required=True,
    )

    umid = forms.CharField(
        required=False,
        validators=[RegexValidator(r'^\d{8,8}$', 'Enter a valid UMID')],
    )

    alumniID = forms.CharField(
        required=False,
        validators=[RegexValidator(r'^\d{7,10}$', 'Enter a valid Alumni ID')],
    )

    ssn = forms.CharField(
        required=False,
        validators=[RegexValidator(r'^\d{4,4}$', 'Enter a 4 digit number')],
    )

