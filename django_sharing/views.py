import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context
import pandas as pd

from rentdivision import robust_rental_harmony

def main(request):
    """Render the main page."""
    with open('django_sharing/templates/index.html') as f:
        t = Template(f.read())
        return HttpResponse(t.render(Context({})))


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

    return HttpResponse(json.dumps({
        'solution': repr(solution),
        'envies': repr(envies),
        'envyFree': envy_free,
    }))

    return HttpResponse(output+"\nWhere the data was: \n%s" % preferences)


