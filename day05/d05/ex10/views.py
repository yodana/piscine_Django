from django.shortcuts import render
from django.http import HttpResponse
from ex10.models import People, Planets, Movies
from django.template import loader
from .forms import SearchForm

def init(request):
    form = SearchForm()
    template = loader.get_template('ex10_form.html')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            result = []
            planet_diameter = form.cleaned_data['planet_diameter']
            min_date = form.cleaned_data['min_date']
            max_date = form.cleaned_data['max_date']
            gender = form.cleaned_data['gender']
            movies = Movies.objects.filter(
                release_date__range=(min_date, max_date)
            )
            for movie in movies:
                peoples = movie.characters.filter(gender=gender, homeworld__diameter__gte=planet_diameter)
                for people in peoples:
                    result.append(f"<p>{movie}-{people.name}-{people.gender}-{people.homeworld}-{people.homeworld.diameter}</p>")
            if result == []:
                result = ["Nothing corresponding to your research"]
            return HttpResponse(template.render({'form': form, 'peoples': result}, request))
        else:
            return HttpResponse(template.render({'form': form}, request))
    return HttpResponse(template.render({'form': form}, request))