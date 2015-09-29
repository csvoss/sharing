import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context
import pandas as pd
import simplejson

from rentdivision import robust_rental_harmony

def main(request):
    """Render the main page."""
    with open('django_sharing/templates/index.html') as f:
        t = Template(f.read())
        return HttpResponse(t.render(Context({})))

# https://coderwall.com/p/k8vb_a/returning-json-jsonp-from-a-django-view-with-a-little-decorator-help
def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = simplejson.dumps(objects)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = simplejson.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator



@json_response
def split_rent(request):
    """Calculate the split rent using Critch's code."""
    preferences = request.GET.get("preferences")
    total_rent = request.GET.get("totalRent")

    try:
        total_rent = int(total_rent)
    except ValueError:
        return HttpResponseBadRequest("totalRent must be an integer.")

    try:
        pydict = json.loads(preferences)
        values = pd.DataFrame(pydict).T
    except ValueError:
        return HttpResponseBadRequest("preferences is invalid.")

    solution, envies, envy_free = robust_rental_harmony.rental_harmony(
        total_rent, values)

    return {
        'solution': repr(solution),
        'envies': repr(envies),
        'envyFree': envy_free,
    }
