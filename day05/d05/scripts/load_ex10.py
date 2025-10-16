from ex10.models import People, Planets, Movies
import json

def run():
    with open('../ex10_initial_data.json', 'r') as f:
        data = json.load(f)
        tab_planets = []
        for item in data:
            if item["model"] == "ex10.planets":
                Planets.objects.get_or_create(
                    name=item['fields']['name'],
                    defaults={
                        'climate': item['fields']['climate'],
                        'diameter': item['fields']['diameter'],
                        'orbital_period': item['fields']['orbital_period'],
                        'population': item['fields']['population'],
                        'rotation_period': item['fields']['rotation_period'],
                        'surface_water': item['fields']['surface_water'],
                        'terrain': item['fields']['terrain']
                    })
                if [item['fields']['name'], item['pk']] not in tab_planets:
                    tab_planets.append([item['fields']['name'], item['pk']])
            elif item["model"] == "ex10.people":
                homeworld_planet = None
                if item['fields']['homeworld'] != None:
                    for planet in tab_planets:
                        if planet[1] == item['fields']['homeworld']:
                            homeworld_planet = Planets.objects.get(name=planet[0])
                item = item['fields']
                People.objects.get_or_create(
                    name=item['name'],
                    defaults={
                        'birth_year': item['birth_year'],
                        'gender': item['gender'],
                        'eye_color': item['eye_color'],
                        'hair_color': item['hair_color'],
                        'height': item['height'],
                        'mass': item['mass'],
                        'homeworld': homeworld_planet
                    })
            else:
                characters = []
                for item_characters in item['fields']['characters']:
                    characters.append(People.objects.get(id=item_characters))
                movie, created = Movies.objects.get_or_create(
                    title=item['fields']['title'],
                    defaults={
                        'episode_nb': item['pk'],
                        'opening_crawl': item['fields']['opening_crawl'],
                        'director': item['fields']['director'],
                        'producer': item['fields']['producer'],
                        'release_date': item['fields']['release_date'],
                    })
                movie.characters.set(characters)