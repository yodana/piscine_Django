from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from datetime import datetime
import os
from django.conf import settings

def ex02(request):
    template = loader.get_template('form.html')
    hist = []
    path_log = settings.PATH_LOG
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            try:
                with open(path_log, 'a') as f:
                    f.write(form.cleaned_data['name'] + " " + str(datetime.now()) + '\n')
            except Exception as e:
                raise e
    else:
        form = NameForm()
    try:
        if os.path.exists(path_log):
            with open(path_log, 'r') as f:
                for line in f:
                    hist.append(line)
    except Exception as e:
        raise e
    return HttpResponse(template.render({'form': form, 'hist': hist}, request))
