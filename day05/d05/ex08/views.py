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
            CREATE TABLE IF NOT EXISTS ex08_planets (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) NOT NULL UNIQUE,
            climate TEXT,
            diameter INT,
            orbital_period INT,
            population BIGINT,
            rotation_period INT,
            surface_water REAL,
            terrain VARCHAR(128)
            );""")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) NOT NULL UNIQUE,
            birth_year VARCHAR(32),
            gender VARCHAR(32),
            eye_color VARCHAR(32),
            hair_color VARCHAR(32),
            height INT,
            mass REAL,
            homeworld VARCHAR(64),
            FOREIGN KEY (homeworld) REFERENCES ex08_planets(name));
        """)
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        return HttpResponse("KO " + str(e))
    return HttpResponse('OK')

def populate(request):
    conn = connect()
    if isinstance(conn, HttpResponse):
        return conn
    try:
        cur = conn.cursor()
        with open('ex08/data/planets.csv', 'r') as f:
            cur.copy_from(f, 'ex08_planets', sep='\t', columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'), null='NULL')
        with open('ex08/data/people.csv', 'r') as f:
            cur.copy_from(f, 'ex08_people', sep='\t', columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'), null='NULL')
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        if "already exists" in str(e):
            return HttpResponse("KO " + "Table already exists")
        return HttpResponse("KO " + str(e))
    return HttpResponse('OK')

def display(request):
    conn = connect()
    if isinstance(conn, HttpResponse):
        return HttpResponse("Not data available")
    try:
        cur = conn.cursor()
        cur.execute("SELECT people.name, people.homeworld, planet.climate FROM ex08_people people INNER JOIN ex08_planets planet ON people.homeworld = planet.name")
        tab = cur.fetchall()
        result = []
        if len(tab) == 0:
            return HttpResponse("Not data available")
        for people in tab:
            climate = people[2]
            windy = False
            if climate != None and "windy" in climate:
                windy = True
                climate = climate.replace("windy", "")
            if climate != None:
                climate = climate.replace(",", "")
            result.append(f"<tr><td>{people[0]}</td><td>{people[1]}</td><td>{climate}</td><td>{windy}</td></tr>")
        cur.close()
    except psycopg2.Error as e:
        return HttpResponse("Not data available" + str(e))
    template = loader.get_template('ex08_display.html')
    return HttpResponse(template.render({'result': result}, request))