from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import psycopg2


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
        CREATE TABLE IF NOT EXISTS ex00_movies (
        title VARCHAR(64) NOT NULL UNIQUE,
        episode_nb INT PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
        )""")
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        return HttpResponse("KO " + str(e))
    return HttpResponse('OK')
