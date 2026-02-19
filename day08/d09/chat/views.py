from django.shortcuts import render
from chat.models import *
from django.contrib.auth.decorators import login_required


def ShowsRoom(request):
    if Room.objects.count() == 0:
        Room.objects.create(room_name='room_1')
        Room.objects.create(room_name='room_2')
        Room.objects.create(room_name='room_3')
    return render(request, 'index.html', {'rooms': Room.objects.all()})

@login_required(login_url='/account/')
def MessageView(request, room_name):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room).order_by('-created')[:3]   
    get_messages = reversed(get_messages)
    #for message in get_messages:
    #    print(message.message)
    get_user_connected = UsersConnected.objects.filter(room=get_room, user=request.user.username)
    #UsersConnected.objects.all().delete()
    if get_user_connected.exists():
        user_connected = True
    else:
        user_connected = False
    print(user_connected)
    context = {
        "messages": get_messages,
        "user": request.user.username,
        "room_name": room_name,
        "user_connected": user_connected,
    }
    
    return render(request, 'message.html', context)
