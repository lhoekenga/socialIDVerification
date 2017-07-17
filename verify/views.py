from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import VerifyForm

from django.http import Http404
from .validate import validate_form_data 
from .cirrus_jwt import generate_jwt

import logging

logger = logging.getLogger(__name__)

def verify(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VerifyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            logger.debug('form={}'.format(scrub_ssn(form.cleaned_data.copy())))
            entry = validate_form_data(form)
            if entry:
                logger.debug('entry={}'.format(entry))
                # redirect to a new URL:
                cirrus_proxy_url = generate_jwt(entry)
                return redirect('confirmed')
            else:
                form.add_error(None, 'Unable to validate identity')
        else:
            logger.warn('form.errors={}'.format(form.errors.as_json(escape_html=False)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VerifyForm()

    return render(request, 'verify.html', {'form': form})

def confirmed(request):
    return HttpResponse("It's you!")


def scrub_ssn(cleaned_form):
    if cleaned_form['ssn']:
        cleaned_form['ssn'] = 'xxxx'
    return cleaned_form
