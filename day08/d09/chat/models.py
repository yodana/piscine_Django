from django.db import models
import uuid 

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()
    connected = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=255)

    def __str(self):
        return str(self.room)

class UsersConnected(models.Model):
    user = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    nbr_connected = models.IntegerField(default=0)
    