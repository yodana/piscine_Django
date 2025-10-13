import sys

def capital_city(city):    
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if city in capital_cities.values():
        for key, val in capital_cities.items():
            if val == city:
                r = key
        for key, val in states.items():
            if val == r:
                print(key)
    else:
        print("Unknown")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])