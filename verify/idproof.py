from django.conf import settings

from .utils import scrub_ssn

import requests
import json
import logging

logger = logging.getLogger(__name__)

# We expect form.cleaned_data to be passed
def idproof_form_data(form_cleaned_data):

    try:
        cert = (settings.IDPROOF_CERT, settings.IDPROOF_KEY)

        payload = {
            'firstName': form_cleaned_data['first_name'],
            'lastName': form_cleaned_data['last_name'],
            'birthdate': form_cleaned_data['birth_date'].strftime('%m/%d/%Y'),
            'degree': form_cleaned_data['degree_year'],
            'umId': form_cleaned_data['umid'],
            'alumniId': form_cleaned_data['alumniID'],
            'ssn': form_cleaned_data['ssn'],
        }
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

        logger.debug('Calling url={} with payload={}'.format(settings.IDPROOF_URL, json.dumps(scrub_ssn(payload))))

        r = requests.post(
            settings.IDPROOF_URL,
            data=json.dumps(payload),
            headers=headers,
            cert=cert,
        )
        try:
            logger.debug('response={} json={}'.format(r, r.json()))
        except:
            logger.warn('Unable to json_decode response={}'.format(r))
            raise
        r.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logger.error('HTTPError={}'.format(e))
        return False

    except Exception as e:
        logger.error('BaseException={}'.format(e))
        return False

    logger.info('form data has successfully validated')
    return r.json()


