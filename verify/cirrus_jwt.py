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
        eppn = entry['umichRegUid'][0] + '@umich.edu'
        dirId = entry['umichDirectoryID'][0].replace('-', 'x')
        cirrusAttributes = {
            'alumniId': entry['umichOudDacID'][0],
            'alumniEmail': entry['umichOudPrefEmailAddress'][0],
            'eduPersonUniqueId': dirId,
            'employeeNumber': entry['umichRegEntityID'][0],
            'eppn': eppn,
        }

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
        key = settings.CERT_DIR + settings.JWT_PRIVATE_KEY
        private_key = open(key, 'r').read()  # RSA key in PEM format
        token = jwt.encode(payload, key=private_key, algorithm='RS256', headers={'kid': settings.JWT_KEY_ID})
        #logger.debug('token={}'.format(token))

    except Exception as e:
        logger.error('exception={}'.format(e))

    return token
