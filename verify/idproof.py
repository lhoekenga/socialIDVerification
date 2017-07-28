import requests
import json
import logging

logger = logging.getLogger(__name__)

def idproof_form_data(verify_form):

    try:
        payload = {
            'firstName': verify_form.cleaned_data['first_name'],
            'lastName': verify_form.cleaned_data['last_name'],
            'birthdate': verify_form.cleaned_data['birth_date'].strftime('%m/%d/%Y'),
            'degree': verify_form.cleaned_data['degree_year'],
            'umId': verify_form.cleaned_data['umid'],
            'alumniId': verify_form.cleaned_data['alumniID'],
            'ssn': verify_form.cleaned_data['ssn'],
        }
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

        logger.debug('payload={}'.format(payload))

        r = requests.post('https://identityproof-dev.dsc.umich.edu/identityproof/search', data=json.dumps(payload), headers=headers)
        logger.deubg('response.json={}'.format(r.json()))
        r.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logger.error('HTTPError={}'.format(e))
        return False

    except Exception as e:
        logger.error('BaseException={}'.format(e))
        return False

    logger.info('form data has successfully validated')
    return r.json()

