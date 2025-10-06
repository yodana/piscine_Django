import sys
import requests
from bs4 import BeautifulSoup


def parser(soup):
    soup = soup.find('div', class_='mw-body-content')
    resultat = soup.find_all('p')
    for p in resultat:
        for link in p.find_all('a'):
            if (link.get('href').startswith('/wiki/')) and ":" not in link.get('href'):
                return link.get('href').split('/')[-1]
    return -1 

def get_page(name):
    url = f"https://en.wikipedia.org/w/index.php?search={name}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
    except requests.HTTPError as e:
        raise e
    return r.text

if __name__ == '__main__':
    # Test dead end Celina_Olga_Moniz
    # Test infinite loop
    if len(sys.argv) == 2:
        name = sys.argv[1]
        roads_to_philosophy = []
        i = 0
        while "Philosophy" not in roads_to_philosophy:
            page = get_page(name)
            soup = BeautifulSoup(page, 'html.parser')
            if soup.h1.text == "Search results":
                print("It leads to a dead end !")
                break
            if soup.h1.text in roads_to_philosophy:
                print("It leads to an infinite loop !")
                break
            roads_to_philosophy.append(soup.h1.text)
            print(soup.h1.text)
            name = parser(soup)
            if name == -1:
                print("It leads to a dead end !")
                break
            i += 1
        if "Philosophy" in roads_to_philosophy:
            print(f"{i+1} roads from {sys.argv[1]} to philosophy")