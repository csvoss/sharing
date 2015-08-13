from django.http import HttpResponse
from django.template import Template, Context

def main(request):
    """Render the main page."""
    with open('django_sharing/templates/index.html') as f:
        t = Template(f.read())
        return HttpResponse(t.render(Context({})))


def split_rent(request):
    """Calculate the split rent using Critch's code."""
    data = request.GET.get("user_input");
    return HttpResponse("(Output of Critch's code on the data here)\nWhere the data was: \n%s" % data)


