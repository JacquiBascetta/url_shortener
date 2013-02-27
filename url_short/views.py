from django.shortcuts import render_to_response
from url_short.models import ShortLinkForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def find_origurl(request):
    if request.method == 'POST': #if a form has been submitted
        form=ShortLinkForm(request.POST)
        if form.is_valid():
            url = form.save()
            return HttpResponseRedirect('/thanks/') #filled out properly, redirects
    else:
        form = ShortLinkForm() #gives unbound form
    return render_to_response('form.html', {
        'form': ShortLinkForm(),
        })



