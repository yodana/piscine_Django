from ex09.models import People, Planets
import json

def run():
    with open('../ex09_initial_data.json', 'r') as f:
        data = json.load(f)
        print(data)
        tab_planets = []
        for item in data:
            print(item)
            if item["model"] == "ex09.planets":
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
            else:
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
