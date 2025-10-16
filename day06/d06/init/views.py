from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.template import loader
import random
import time 
from .forms import RegisterForm, LoginForm, TipForm
from .models import MyUser, Tip
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def init(request):
    template = loader.get_template('base.html')
    form = ""
    tips = Tip.objects.all()
    if request.user.is_authenticated:
        form = TipForm()
        result = []
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                contenu = form.cleaned_data['contenu']
                auteur = request.user
                tip = Tip.objects.create(contenu=contenu, auteur=auteur)
                return redirect('/')
        return HttpResponse(template.render({"username": request.user.username, 
        "form": form, 
        "tips": tips}
        , request))
    else:
        if request.session.get('username') == None or time.time() - request.session["time"] >= 42:
            request.session["username"] = random.choice(settings.USERNAMES)
            request.session["time"] = time.time()
    return HttpResponse(template.render({"username": request.session.get('username'), "tips": tips}, request))


def verif_user(username, password, verif_password):
    if password != verif_password:
        return "Passwords don't match"
    else:
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist: 
            return None
    return "Username already taken"

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    template = loader.get_template('register.html')
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            verif_password = form.cleaned_data['verif_password']
            error = verif_user(username, password, verif_password)
            if error == None:
                user = MyUser.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('init')
    return HttpResponse(template.render({'username':request.session.get('username'), 'form': form, 'error':error}, request))

def mylogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    error = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["username"] = username
                return redirect('/')
            elif user is None:
                error = "Username or password is incorrect"       
    template = loader.get_template('register.html')
    return HttpResponse(template.render({'username':request.session.get('username'), 'form': form, 'error':error}, request))

def mylogout(request):
    logout(request)
    print(request.user.is_authenticated)
    return redirect('/')

def maj_rep(user):
    if user.reputation >= 15:
        user.can_downvote = True
    else:
        user.can_downvote = True
    if user.reputation >= 30:
        user.has_permission = True
    else:
        user.has_permission = False
    user.save()

@login_required
def mydelete(request, id):
    if request.method == 'POST':
        if request.user.has_permission or request.user == Tip.objects.get(id=id).auteur:
            tip = Tip.objects.get(id=id)
            if tip.downvote.count() > tip.upvote.count() or request.user == tip.auteur:
                points = tip.downvote.count() * 2
                tip.auteur.reputation += points
                points = tip.upvote.count() * 5
                tip.auteur.reputation -= points
                tip.auteur.save()
                maj_rep(tip.auteur)
                tip.delete()
    return redirect('/')

@login_required
def upvote(request, id):
    if request.method == 'POST':
        tip = Tip.objects.get(id=id)
        if request.user in tip.downvote.all():
            tip.downvote.remove(request.user)
            tip.auteur.reputation += 2
            tip.auteur.save()
        else:
            if request.user not in tip.upvote.all():
                tip.auteur.reputation += 5
                tip.upvote.add(request.user)
                tip.auteur.save()
    maj_rep(tip.auteur)
    return redirect('/')

@login_required
def downvote(request, id):
    if request.method == 'POST':
        if request.user.can_downvote or request.user == Tip.objects.get(id=id).auteur:
            tip = Tip.objects.get(id=id)
            if request.user in tip.upvote.all():
                tip.upvote.remove(request.user)
                tip.auteur.reputation -= 5
                tip.auteur.save()
            elif request.user not in tip.downvote.all():
                tip.auteur.reputation -= 2
                tip.auteur.save()
                tip.downvote.add(request.user)
        maj_rep(tip.auteur)
        return redirect('/')