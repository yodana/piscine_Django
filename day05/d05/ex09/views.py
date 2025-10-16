from django.shortcuts import render
from django.http import HttpResponse
from ex09.models import People, Planets
from django.template import loader

def display(request):
    try:
        result = []
        tab = People.objects.all().order_by('name')
        if len(tab) == 0:
            return HttpResponse("No data available, please use the following command line before use: python3 manage.py runscript load_people")
        for people in tab:
            windy = False
            if people.homeworld != None:
                if people.homeworld.climate != None:
                    if "windy" in people.homeworld.climate:
                        windy = True
                    climate = people.homeworld.climate.replace("windy", "").replace(",", "")
            result.append(f"<tr><td>{people}</td><td>{people.homeworld}</td><td>{climate}</td><td>{windy}</td></tr>")
    except Exception as e:
        return HttpResponse("Not data available" + str(e))
    template = loader.get_template('ex09_display.html')
    return HttpResponse(template.render({'result': result}, request))