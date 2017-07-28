from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings

from urllib.parse import quote_plus
from .forms import VerifyForm
from .idproof import idproof_form_data 
from .cirrus_jwt import generate_jwt

import logging

logger = logging.getLogger(__name__)

def verify(request):
    # if this is a POST request we need to process the form data
    logger.info(request)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VerifyForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            logger.debug('form={}'.format(scrub_ssn(form.cleaned_data.copy())))
            entry = idproof_form_data(form)

            # if we have an entry, then idproof was successful, so get jwt and sent them to cirrus:
            if entry:
                logger.debug('entry={}'.format(entry))
                jwt = generate_jwt(entry)
                cirrus_url = 'https://{}.proxy.cirrusidentity.com/module.php/cirrusaccountlink/link.php?idVerifyToken={}'.format(settings.TENANT_ID, quote_plus(jwt))
                logger.info('Redirecting user to {}'.format(cirrus_url))
                return redirect(cirrus_url)
            # If unable to idproof, return the form with an error message:
            else:
                form.add_error(None, settings.VALIDATION_ERROR_MESSAGE)
        # If form is invalid, then return the form with error messages
        else:
            logger.warn('form.errors={}'.format(form.errors.as_json(escape_html=False)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VerifyForm()

    return render(request, 'verify.html', {'form': form})


# For logging purposes
def scrub_ssn(cleaned_form):
    if cleaned_form['ssn']:
        cleaned_form['ssn'] = 'xxxx'
    return cleaned_form
