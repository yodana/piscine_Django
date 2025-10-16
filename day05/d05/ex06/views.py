from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import psycopg2
from .forms import DeleteForm

def connect():
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="formationdjango",
            user="djangouser",
            password="secret"
        )
        return conn
    except psycopg2.Error as e:
        return HttpResponse("KO " + str(e))

def init(request):
    conn = connect()
    if isinstance(conn, HttpResponse):
        return conn
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex06_movies (
            title VARCHAR(64) NOT NULL UNIQUE,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL,
            created TIMESTAMP NOT NULL DEFAULT NOW(),
            updated TIMESTAMP NOT NULL DEFAULT NOW()
            )""")
        cur.execute("""
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
        """)
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        return HttpResponse("KO " + str(e))
    return HttpResponse('OK')

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
    conn = connect()
    if isinstance(conn, HttpResponse):
        return conn
    try:
        cur = conn.cursor()
        insert_query = """
            INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (episode_nb) DO NOTHING;
            """
        for movie in movies_data:
            data = (movie['episode_nb'], movie['title'], movie['director'], movie['producer'], movie['release_date'])
            cur.execute(insert_query, data)
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        return HttpResponse("KO " + movie["title"] + " " + str(e)) 
    return HttpResponse('OK')

def display(request):
    conn = connect()
    if isinstance(conn, HttpResponse):
        return HttpResponse("Not data available")
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex06_movies")
        tab = cur.fetchall()
        result = []
        if len(tab) == 0:
            return HttpResponse("Not data available")
        for movie in tab:
            result.append(f"<tr><td>{movie[0]}</td><td>{movie[1]}</td><td>{movie[2]}</td><td>{movie[3]}</td><td>{movie[4]}</td><td>{movie[5]}</td><td>{movie[6]}</td><td>{movie[7]}</td></tr>")
        cur.close()
    except psycopg2.Error as e:
        return HttpResponse("Not data available")
    template = loader.get_template('ex06_display.html')
    return HttpResponse(template.render({'result': result}, request))

def update(request):
    conn = connect()
    if isinstance(conn, HttpResponse):
        return HttpResponse("Not data available")
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex06_movies")
        form = DeleteForm()
        movies = cur.fetchall()
        if len(movies) == 0:
            return HttpResponse("Not data available")
        form.fields['title'].choices = [(movie[1], movie[0]) for movie in movies]
    except psycopg2.Error as e:
        return HttpResponse("Not data available")
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        form.fields['title'].choices = [(movie[1], movie[0]) for movie in movies]
        if form.is_valid():
            id_title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            try:
                cur.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE episode_nb = %s", (description, id_title))
                conn.commit()
            except psycopg2.Error as e:
                return HttpResponse("Not data available" + str(e))
        return HttpResponse('OK Update done')
    cur.close()
    template = loader.get_template('update.html')
    return HttpResponse(template.render({'form': form}, request))