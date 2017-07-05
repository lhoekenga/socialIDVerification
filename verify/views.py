from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import VerifyForm

from django.http import Http404
from .validate import validate_form_data 
from .cirrus_jwt import generate_jwt

def index(request):
    return HttpResponse("Hello, world")

def verify(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VerifyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            entry = validate_form_data(form)
            if entry:
                # redirect to a new URL:
                cirrus_proxy_url = generate_jwt(entry)
                return redirect('confirmed')
            else:
                raise Http404('No match found')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VerifyForm()

    return render(request, 'verify.html', {'form': form})

def confirmed(request):
    return HttpResponse("It's you!")

