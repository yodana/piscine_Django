from django.http import HttpResponse
from django.template import loader

def django(request):
    template = loader.get_template('django.html')
    return HttpResponse(template.render())

def template(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())

def affichage(request):
    template = loader.get_template('affichage.html')
    return HttpResponse(template.render())