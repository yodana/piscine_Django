from Page import Page
from elements import Tp,  Html, Head, Body, Title, Meta, Img, Table, Tr, Td, Th, Ul, Ol, Li, H1, H2, P, Span, Br, Div, Hr
from elem import Text
if __name__ == '__main__':
    # False not the right elem
    '''print(Page([Html([Head(), Hr(), Tp()])]).is_valid())
    # False Html rule
    print(Page([Html([Head(), Hr(), Body()])]).is_valid())
    # True Html rule
    print(Page([Html([Head(Title(Text("test title"))), Body()])]).is_valid())
    # False Head rule
    print(Page([Html([Head([Title(Text("test title")), Title(Text("test title"))]), Body()])]).is_valid())
    print(Page([Html([Head(Title(Text("test title"))), Body()])]).is_valid())
    # True False body and div rule
    print(Page([Html([Head(Title(Text("test title"))), Body(Body())])]).is_valid())
    print(Page([Html([Head(Title(Text("test title"))), Body(Div())])]).is_valid()) 
    # Title text rule
    print(Page([Html([Head(Title(Text('Hello world!'))), Body()])]).is_valid())
    print(Page([Html([Head(Title(Head()))], Body())]).is_valid())
    # P rule
    print(Page([P(Text('Hello world!'))]).is_valid())
    print(Page([P(P())]).is_valid())
    #Ul ol rule
    print("Ul ol rule")
    print(Page([Ul([Li(Text("test"))])]).is_valid())
    print(Page([Ol([Li(Text("test"))])]).is_valid())
    print(Page([Ul([(Text('Hello world!')), Li()])]).is_valid())
    # Tr rule
    print(Page([Table([Tr([Th(Text('Hello world!')), Td()])])]).is_valid())
    print(Page([Table([Tr(Text('Hello world!')), Tr(Text('Hello world!'))])]).is_valid())
    #Table rule
    print(Page([Table([Tr([Th(Text('Hello world!')), Td(Text('Hello world!'))])])]).is_valid())'''
    print(Page(Div(Text('Hello world!'))))
    print(Page(Html([Head(Title(Text('Hello world!'))), Body(Div(Text('Hello world!')))])))
    Page(Html([Head(Title(Text('Hello world!'))), Body(Div(Text('Hello world!')))])).write_to_file()