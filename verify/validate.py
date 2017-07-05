from ldap3 import Server, Connection, ALL


def validate_form_data(verify_form):

    try:
        print('hello from validate')

        # just fake it for now
        entry = {
            'umichRegDisplayGivenName': ['mega'],
            'umichRegDisplaySurname': ['man'],
            'umichRegUid': ['megaman'],
            'umichRegEntityID': ['13371337'],
            'umichDirectoryID': ['999-999-13379999999999999-999'],
            'umichOudDacID': ['0011223344'],
            'umichOudPrefEmailAddress': ['megaman@gmail.com'],
        }

        if entry['umichRegDisplaySurname'][0].lower() == verify_form.cleaned_data['last_name'].lower():
            print('last name matches')
        else:
            raise('last name does not match!')

        if entry['umichRegDisplayGivenName'][0].lower() == verify_form.cleaned_data['first_name'].lower():
            print('first name matches')
        else:
            raise('first name does not match!')

    except Exception as e:
        print('e={}'.format(e))
        return False

    return entry


