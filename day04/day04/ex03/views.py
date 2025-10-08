from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def ex03(request):
    template = loader.get_template('tab.html')
    color = ['0, 0 , 0', '255, 0 , 0', '0, 0 , 255', '0, 255 , 0']
    name_color = ['black', 'red', 'blue', 'green']
    tab = []
    a = 1
    for i in range(51):
        tr_add = '<tr>'
        if i == 0:
            for i in range(4):
                tab.append(f'{tr_add}<th height="40px" width="80px" style="border: 1px solid black;">{name_color[i]}</th>')
                tr_add = ""
        else:
            for i in range(4):
                tab.append(f'{tr_add}<td height="40px" width="80px" style="background-color: rgba({color[i]}, {a});"></td>')
                tr_add = ""
        a = a - 0.014
        tab[-1] = tab[-1] + '</tr>'
    return HttpResponse(template.render({'tab': tab}, request))