from django.http import HttpResponse, HttpResponseNotFound, Http404
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def past_datetime(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


# TODO Customize error views
def datetime_404(request):
    raise Http404("I'm fucked up")
