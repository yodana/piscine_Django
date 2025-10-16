from django.shortcuts import render
from django.http import HttpResponse
from ex07.models import Movie
from django.template import loader
from .forms import DeleteForm

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
            Movie.objects.get_or_create(
                episode_nb=movie['episode_nb'],
                defaults={
                    'title': movie['title'],
                    'opening_crawl': "",
                    'director': movie['director'],
                    'producer': movie['producer'],
                    'release_date': movie['release_date']
                }
            )
    except Exception as e:
        return HttpResponse("KO " + str(e))
    return HttpResponse('OK')

def display(request):
    try:
        movies = list(Movie.objects.all().values())
        result = []
        if len(movies) == 0:
                return HttpResponse("Not data available")
        print(movies)
        for movie in movies:
            result.append(f"<tr><td>{movie['title']}</td><td>{movie['episode_nb']}</td><td>{movie['opening_crawl']}</td><td>{movie['director']}</td><td>{movie['producer']}</td><td>{movie['release_date']}</td><td>{movie['created']}</td><td>{movie['updated']}</td></tr>")
    except Exception as e:
        return HttpResponse("Not data available")
    template = loader.get_template('ex07_display.html')
    return HttpResponse(template.render({'result': result}, request))

def update(request):
    try:
        movies = list(Movie.objects.all().values())
        result = []
        form = DeleteForm()
        if len(movies) == 0:
            return HttpResponse("Not data available")
        form.fields['title'].choices = [(movie["episode_nb"], movie["title"]) for movie in movies]
    except Exception as e:
        return HttpResponse("Not data available")
    if request.method == 'POST':
        try:
            form = DeleteForm(request.POST)
            form.fields['title'].choices = [(movie["episode_nb"], movie["title"]) for movie in movies]
            if form.is_valid():
                id_title = form.cleaned_data['title']
                movie = Movie.objects.get(episode_nb=id_title)
                movie.opening_crawl = form.cleaned_data['description']
                movie.save()
                return HttpResponse('OK Update done')
        except Exception as e:
            return HttpResponse("Not data available")
    template = loader.get_template('ex07_update.html')
    return HttpResponse(template.render({'form': form}, request))

