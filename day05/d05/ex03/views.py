from django.shortcuts import render
from django.http import HttpResponse
from ex03.models import Movie
from django.template import loader

def populate(request):
    movies_data = [
    {
        'episode_nb': 1,
        'title': 'The Phantom Menace',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '1999-05-19'
    },
    {
        'episode_nb': 2,
        'title': 'Attack of the Clones',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2002-05-16'
    },
    {
        'episode_nb': 3,
        'title': 'Revenge of the Sith',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2005-05-19'
    },
    {
        'episode_nb': 4,
        'title': 'A New Hope',
        'director': 'George Lucas',
        'producer': 'Gary Kurtz, Rick McCallum',
        'release_date': '1977-05-25'
    },
    {
        'episode_nb': 5,
        'title': 'The Empire Strikes Back',
        'director': 'Irvin Kershner',
        'producer': 'Gary Kutz, Rick McCallum',
        'release_date': '1980-05-17'
    },
    {
        'episode_nb': 6,
        'title': 'Return of the Jedi',
        'director': 'Richard Marquand',
        'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
        'release_date': '1983-05-25'
    },
    {
        'episode_nb': 7,
        'title': 'The Force Awakens',
        'director': 'J. J. Abrams',
        'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
        'release_date': '2015-12-11'
    }
    ]
    try:
        for movie in movies_data:
            tabl = Movie(movie['title'], movie['episode_nb'], "", movie['director'], movie['producer'], movie['release_date'])
            tabl.save()
    except Exception as e:
        return HttpResponse("KO " + str(e))
    return HttpResponse('OK')

def display(request):
    try:
        movies = list(Movie.objects.all().values())
        print(movies)
        result = []
        if len(movies) == 0:
                return HttpResponse("Not data available")
        for movie in movies:
            result.append(f"<tr><td>{movie['title']}</td><td>{movie['episode_nb']}</td><td>{movie['opening_crawl']}</td><td>{movie['director']}</td><td>{movie['producer']}</td><td>{movie['release_date']}</td></tr>")
    except Exception as e:
        return HttpResponse("Not data available " + str(e))
    template = loader.get_template('display.html')
    return HttpResponse(template.render({'result': result}, request))