import jwt
import time
import uuid

from django.conf import settings

import logging
logger = logging.getLogger(__name__)

def generate_jwt(entry):

    epoch_time = int(time.time())
    exp_time = epoch_time + 300
    eppn = entry['umichRegUid'][0] + '@umich.edu'
    dirId = entry['umichDirectoryID'][0].replace('-', 'x')
    cirrusAttributes = {
        'alumniId': entry['umichOudDacID'][0],
        'alumniEmail': entry['umichOudPrefEmailAddress'][0],
        'dirId': dirId,
        'employeeNumber': entry['umichRegEntityID'][0],
        'eppn': eppn,
    }

    payload = {
        'aud': 'umich-uat',
        'lat': epoch_time,
        'exp': exp_time,
        'jti': str(uuid.uuid4()),
        'sub': dirId,
        'cirrusAttributes': cirrusAttributes,
    }

    logger.debug('payload={}'.format(payload))
    key = settings.CERT_DIR + 'private_key.pem'
    private_key = open(key, 'r').read()  # RSA key in PEM format
    encoded = jwt.encode(payload, key=private_key, algorithm='RS256', headers={'kid': 'k1'})

    logger.debug('jwt={}'.format(encoded))
    return encoded
