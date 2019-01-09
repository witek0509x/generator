from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('main_page/index.html')
    contex = {}
    return HttpResponse(template.render(contex, request))
