from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    owner  = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    created_at = models.DateField(auto_now=True )
    users = models.TextField(default="[]")
    
    def __str__(self) :
        return self.name
    


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now=True )
    sender_name = models.TextField()
    
    
    def get_sender_name(self):
        return self.sender_name
    
    def __str__(self):
        return self.content
    
    
