
from django.http import HttpResponse


def helloView(req):
    return HttpResponse('Bonjour tout le monde')