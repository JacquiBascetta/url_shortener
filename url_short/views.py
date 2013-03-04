from django.shortcuts import render_to_response
from url_short.form import ShortLinkForm
from url_short.models import ShortLink
from django.http import HttpResponseRedirect
from django.template import RequestContext


def find_origurl(request):
    success = False

    if request.method == 'POST': #if a form has been submitted
        link_form = ShortLinkForm(request.POST)
        print link_form['original_URL']

        if link_form.is_valid():
            Success = True

            original_URL = link_form.cleaned_data['original_URL']

            orig_url = ShortLink(original_URL=original_URL)
            orig_url.save()

            orig_url_form = ShortLinkForm()

            return HttpResponseRedirect('/thanks/', thanks.html) #filled out properly, redirects
    else:

        form = ShortLinkForm() #gives unbound form
        #this commented section is just to test function return HttpResponseRedirect('http://www.google.com')

    return render_to_response('form.html', {
        'form': ShortLinkForm(),
    }, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html')