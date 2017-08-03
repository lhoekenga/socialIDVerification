from django.conf import settings

import jwt
import time
import uuid
import json
import logging

logger = logging.getLogger(__name__)

def generate_jwt(entry):

    try:
        # Attributes required/requested by Cirrus
        epoch_time = int(time.time())
        exp_time = epoch_time + 300
        dirId = entry['umichDirectoryID'].replace('-', 'x')

        # DirectoryID is the primary identifier and the only required attribute
        cirrusAttributes = {
            'eduPersonUniqueId': dirId,
        }

        # Add optional identifiers if we have values
        if 'umichRegUid' in entry:
            cirrusAttributes['eppn'] = entry['umichRegUid'] + '@umich.edu'

        if 'umichRegEntityID' in entry:
            cirrusAttributes['employeeNumber'] = entry['umichRegEntityID']

        if 'umichOudDacId' in entry:
            cirrusAttributes['alumniId'] = entry['umichOudDacId']

        if 'umichOudPrefEmailAddress' in entry:
            cirrusAttributes['alumniEmail'] = entry['umichOudPrefEmailAddress']

        # Build the jwt payload
        payload = {
            'aud': 'umich-uat',
            'iat': epoch_time,
            'exp': exp_time,
            'jti': str(uuid.uuid4()),
            'sub': dirId,
            'cirrusAttributes': cirrusAttributes,
        }
        logger.debug('payload={}'.format(payload))

        # Encode the payload
        key = settings.JWT_PRIVATE_KEY
        private_key = open(key, 'r').read()  # RSA key in PEM format
        token = jwt.encode(payload, key=private_key, algorithm='RS256', headers={'kid': settings.JWT_KEY_ID})

    except Exception as e:
        logger.error('exception={}'.format(e))

    return token
