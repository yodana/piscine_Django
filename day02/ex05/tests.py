from elements import Html, Head, Body, Title, Meta, Img, Table, Tr, Td, Th, Ul, Ol, Li, H1, H2, P, Span, Br, Div, Hr
from elem import Text

if __name__ == '__main__':
    print( Html( [Head(), Body()]))
    print(Title(Text('Hello world!')))
    print(Meta())
    print(Img())
    print(Table([Tr([Td(), Td()]), Tr([Td(), Td()])]))
    print(Ul([Li(), Li()]))
    print(H1(Text('Hello world!')))
    print(H2(Text('Hello world!')))
    print(P(Text('Hello world!')))
    print(Span(Text('Hello world!')))
    print(Br())
    print(Div(Text('Hello world!')))
    print(Hr())

    # Test de l exercice 04:
    print(Html(
        [Head(
            [Title(
                Text('Hello ground!'))
                ]),
        Body(
            [H1(
                Text('Oh no, not again!')
                ),
            Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})
            ])        
            ]))