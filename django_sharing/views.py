from django.http import HttpResponse
from django.template import Template, Context

def main(request):
    with open('django_sharing/templates/index.html') as f:
        t = Template(f.read())
        return HttpResponse(t.render(Context({})))

    # return HttpResponse("Hello, world!")
