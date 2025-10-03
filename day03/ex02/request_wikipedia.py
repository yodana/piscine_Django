import requests
import json
import dewiki
import sys

def take_wiki(name):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        text_wiki = requests.get(f"https://fr.wikipedia.org/w/api.php?action=parse&format=json&page={name}&prop=wikitext&formatversion=2", headers=headers)
    except requests.HTTPError as e:
        raise e
    try:
        text_wiki = text_wiki.json()
        if 'error' in text_wiki:
            return -1
        text_wiki = text_wiki['parse']['wikitext']
    except ValueError as e:
        raise e
    while "REDIRECT" in text_wiki:
        redirect = text_wiki.split("REDIRECT")[1].replace('[', '').replace(']', '')
        try:
            text_wiki = requests.get("https://fr.wikipedia.org/w/api.php?action=parse&format=json&page=" + redirect + "&prop=wikitext&formatversion=2", headers=headers)
        except requests.HTTPError as e:
            raise e
        try:
            text_wiki = text_wiki.json()['parse']['wikitext']
        except ValueError as e:
            raise e
    return dewiki.from_string(text_wiki)

def text_to_file(text_wiki, name):
    try:
        with open(f'{name}.wiki', 'w') as f:
            f.write(text_wiki)
    except Exception as e:
        raise e
if __name__ == '__main__':
    if len(sys.argv) == 2:
        text_wiki = take_wiki(sys.argv[1])
        if text_wiki == -1:
            print("Error: The page doesn't exist")
        else:
            text_to_file(text_wiki, sys.argv[1])