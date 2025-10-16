from elements import Html, Head, Body, Title, Meta, Img, Table, Tr, Td, Th, Ul, Ol, Li, H1, H2, P, Span, Br, Div, Hr
from elem import Text

class Page:
    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        if isinstance(self.elem, Html) is True:
            return f'<!DOCTYPE html>\n{str(self.elem)}'
        result = str(self.elem)
        return result

    def is_valid(self):
        return self.recursive_validation(self.elem)

    def write_to_file(self, name="fichier.html"):
        resultat = "" 
        if isinstance(self.elem, Html) is True:
            resultat = f'<!DOCTYPE html>\n{str(self.elem)}'
        else:
            resultat = f'{str(self.elem)}'
        try:
            with open(name, 'w') as f:
                f.write(resultat)
        except Exception as e:
            print(e)

    def recursive_validation(self, elem):
        for e in elem:
            if isinstance(e, Text) is True:
                return True
            if len(e.content) == 1:
                if isinstance(e.content[0], Text) is True:
                    return True
            if len(e.content) != 0:
                if self.recursive_validation(e.content) is False:
                    return False
            if (isinstance(e, (Html, Head, Body, Title, Meta, Img, Table, Tr, Td, Th, Ul, Ol, Li, H1, H2, P, Span, Br, Div, Hr))) is False:
                return False
            if (isinstance(e, Html)) is True:
                if len(e.content) != 2 or e.content[0].tag != 'head' or e.content[1].tag != 'body':
                    return False
            if (isinstance(e, Head)) is True:
                if len(e.content) != 1 or e.content[0].tag != 'title':
                    return False
            if (isinstance(e, Body)) is True or (isinstance(e, Div)) is True:
                for e in e.content:
                    if isinstance(e, (H1, H2, Div, Table, Ul, Ol, Span, Text)) is False:
                        return False
            if e.tag in ['title', 'h1', 'h2', 'li', 'th', 'td']:
                if len(e.content) != 1:
                    return False
                if isinstance(e.content[0], Text) is False:
                    return False
            if e.tag == 'p':
                for e in e.content:
                    if isinstance(e, Text) is False:
                        return False
            if e.tag == 'span':
                for e in e.content:
                    if isinstance(e, (Text, P)) is False:
                        return False
            if e.tag == 'ul' or e.tag == 'ol':
                if len(e.content) == 0:
                    return False
                for e in e.content:
                    if isinstance(e, Li) is False:
                        return False
            if e.tag == 'tr':
                if len(e.content) == 0:
                    return False
                
                for e in e.content:
                    if isinstance(e, (Th, Td)) is False:
                        return False
                    if isinstance(e, type(e.content[0])) is False:
                        return False
            if e.tag == 'table':
                for e in e.content:
                    if isinstance(e, Tr) is False:
                        return False
            
        return True
