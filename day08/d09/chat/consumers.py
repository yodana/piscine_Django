import json
from django.forms.models import model_to_dict
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import *
from datetime import datetime
import uuid

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #await self.destroy_user_connected()
        await self.accept()
        self.user = self.scope["user"] # Get the user from the scope
        self.room_name = f"{self.scope['url_route']['kwargs']['room_name']}"
        user_exists = await self.user_exists(self.user, self.room_name)
        if user_exists:
            response_data = {
                'type': 'error_connected',
            }
            await self.send(text_data=json.dumps({'message': response_data}))
        else:
            await self.channel_layer.group_add(self.room_name, self.channel_name)
            event = {
                'type': 'send_user_connected',
                'user': self.user,
                'room': self.room_name,
            }
            await self.create_user_connected(data=event)
            await self.channel_layer.group_send(self.room_name, event)

    async def disconnect(self, close_code):
        self.user = self.scope["user"]
        await self.create_message(data={'message': self.user.username + ' has left the chat','room_name': self.room_name, 'sender': self.user.username}, connected=True)
        await self.delete_user_deconnected(self.user, self.room_name)
        event = {
                'type': 'send_user_deconnected',
                'user': self.user,
                'room': self.room_name,
            }
        await self.channel_layer.group_send(self.room_name, event)
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        event = {
            'type': 'send_message',
            'message': message,
            'connected': False,
        }
        await self.channel_layer.group_send(self.room_name, event)
    
    async def send_user_deconnected(self, event):
        data = event['user']
        response_data = {
            'type': 'user_deconnected',
            'user': data.username,
            'connected': True,
        }
        await self.send(text_data=json.dumps({'message': response_data}))
        room = await self.get_room(self.room_name)
        users = await self.get_user_connected(room)
        response_data = {
            'type': 'send_user_connected',
            'users': users,
            'connected': True,
        }
        await self.send(text_data=json.dumps({'message': response_data}))

    async def send_user_connected(self, event):
        print(event)
        data = event['user']
        response_data = {
            'type': 'user_connected',
            'user': data.username,
            'connected': True,
        }
        await self.create_message(data={'message': data.username + ' has joined the chat','room_name': self.room_name, 'sender': data.username}, connected=True)
        await self.send(text_data=json.dumps({'message': response_data}))
        room = await self.get_room(self.room_name)
        users = await self.get_user_connected(room)
        response_data = {
            'type': 'send_user_connected',
            'users': users,
            'connected': True,
        }
        await self.send(text_data=json.dumps({'message': response_data}))

    async def send_message(self, event):
        print(event)
        data = event['message']
        response_data = {
                'type': 'send_message',
                'sender': data['sender'],
                'message': data['message'],
                'connected': data['connected'],
        }
        await self.create_message(data=data, connected=data['connected'])
        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def create_message(self, data, connected):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'], connected=connected)
        new_message.save()

    @database_sync_to_async
    def create_user_connected(self, data):
        room_obj = Room.objects.get(room_name=data['room'])
        if UsersConnected.objects.filter(user=data['user'], room=room_obj).exists():
            return
        else:
            new_user_connected = UsersConnected(user=data['user'], room=room_obj)
            new_user_connected.save()

    @database_sync_to_async
    def get_room(self, room_name):
        return Room.objects.get(room_name=room_name)


    @database_sync_to_async
    def user_exists(self, user, room):
        room = Room.objects.get(room_name=room)
        return UsersConnected.objects.filter(user=user, room=room).exists()

    @database_sync_to_async
    def get_user_connected(self, room):
        users = [user.user for user in UsersConnected.objects.filter(room=room)]
        return users

    @database_sync_to_async
    def delete_user_deconnected(self, user, room):
        print(user)
        room_obj = Room.objects.get(room_name=room)
        user = UsersConnected.objects.get(user=user, room=room_obj)
        user.delete()

    @database_sync_to_async
    def destroy_user_connected(self):
        UsersConnected.objects.all().delete()
        
