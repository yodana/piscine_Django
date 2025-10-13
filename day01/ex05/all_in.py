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
    for c in city:
        c = c.title()
        if c in states:
            r = capital_cities[states[c]]
            print(f"{r} is the capital of {c}")
        elif c in capital_cities.values():
            for key, val in capital_cities.items():
                if val == c:
                    r = key
            for key, val in states.items():
                if val == r:
                    print(f"{c} in the capital of {key}")
        else:
            print(f"{c}  is neither a capital city nor a state")

def filter_argv(s):
    if ",," in s:
        return
    s = s.split(",")
    res = []
    for mot in s:
        mot = mot.strip()
        if mot != "":
            res.append(mot)
    
    return res

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filtered_argv = filter_argv(sys.argv[1])
        capital_city(filtered_argv)