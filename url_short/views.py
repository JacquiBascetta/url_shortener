from django.shortcuts import render
from url_short.models import ShortLinkForm
from django.http import HttpResponseRedirect


def find_origurl(request, template_name='findurl/my_form.html'):
    if request.method == 'POST': #if a form has been submitted
        form  = ShortLinkForm(request.POST)
        if form.is_valid():

            url = form.save()
            return HttpResponseRedirect('/thanks') #filled out properly, redirects
    else:
        form = ShortLinkForm() #gives unbound form
    return render(request, template_name, {'form': form})



