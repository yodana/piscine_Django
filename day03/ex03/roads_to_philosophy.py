import sys
import requests
from bs4 import BeautifulSoup

def get_page(name):
    url = f"https://en.wikipedia.org/w/index.php?search={name}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
    except requests.HTTPError as e:
        raise e
    return r.text

if __name__ == '__main__':
    if len(sys.argv) == 2:
        page = get_page(sys.argv[1])
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.prettify()) # Trouver la classe class="mw-body-content"
        # Trouver le premier p de cette classe
        # Trouver le premier a 
        # Refaire un 