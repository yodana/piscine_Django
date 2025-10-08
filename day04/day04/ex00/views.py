from django.http import HttpResponse
from django.template import loader
import requests
from bs4 import BeautifulSoup

def ex00(request):
    url = f"https://en.wikipedia.org/w/index.php?search=Markdown"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
    except requests.HTTPError as e:
        raise e
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find('div', class_='mw-body-content')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'soup': soup,}, request))