from django import forms
from django.core.validators import RegexValidator

# our new form
class VerifyForm(forms.Form):

    first_name = forms.CharField(
        required=True,
        #label='First Name',
        #widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        required=True,
        #label='Last Name',
        #widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    birth_date = forms.DateField(
        required=True,
        #label='Birth Date',
        #widget=forms.DateInput(attrs={'type': 'date'}),
    )

    degree_year = forms.CharField(
        required=True,
        #label='Year of First U-M Degree',
        #min_length=4,
        #max_length=4,
        #widget=forms.TextInput(attrs={'placeholder': 'yyyy'}),
        validators=[RegexValidator(r'^\d{4,4}$', 'Enter a valid four digit year')],
    )

    umid = forms.CharField(
        required=False,
        #label='UMID',
        #min_length=8,
        #max_length=8,
        #help_text='An 8-digit number found on your U-M photo ID card.',
        validators=[RegexValidator(r'^\d{8,8}$', 'Enter a valid UMID')],
    )

    lookupID = forms.CharField(
        required=False,
        #label='Alumni ID',
        #min_length=8,
        #max_length=8,
        #help_text='Alumni ID',
        validators=[RegexValidator(r'^\d{7,10}$', 'Enter a valid Alumni ID')],
    )

    ssn = forms.CharField(
        required=False,
        #label='ssn',
        #min_length=4,
        #max_length=4,
        #help_text='SSN',
        validators=[RegexValidator(r'^\d{4,4}$', 'Enter a 4 digit number')],
    )
