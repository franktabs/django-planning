
from django.http import HttpResponse


def helloView(req):
    return HttpResponse('<h1>PROGRAMMATION</h1>')