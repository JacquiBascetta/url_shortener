from django.shortcuts import render_to_response
from url_short.models import ShortLinkForm, ShortLink
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from url_short.models import randomize
from urlparse import urlparse

def find_origurl(request):
    if request.method == "POST": #if a form has been submitted
        f = ShortLinkForm(request.POST)
        if f.is_valid():
            origURL=(f.cleaned_data['original_URL'])
            parsed = urlparse(origURL)
            if parsed.scheme == '':
                origURL = 'http://' + origURL
            try:
                this = ShortLink.objects.get(original_URL=origURL)
                mini_path = str(this.mini_URL)
            except ShortLink.DoesNotExist:
                mini_path = randomize()
                instance = ShortLink(original_URL=origURL, mini_URL=mini_path)
                instance.save()
            html = "<html><body>Your new URL is: <a href= %s> %s </a></body></html>" % (mini_path, 'parvus.me/' + mini_path)
            return HttpResponse(html)
    else:
        f = ShortLinkForm() #gives unbound form

    return render_to_response('form.html', {'form': f}, context_instance=RequestContext(request))

def redirect_mini(request):
    if request.method == "GET":
        mini_path = request.path_info[1:]
    try:
        site = ShortLink.objects.get(mini_URL=mini_path)
        return HttpResponseRedirect(site.original_URL)
    except ShortLink.DoesNotExist:
        return render_to_response('404.html')
