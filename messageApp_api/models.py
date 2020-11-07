from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)


class Message(models.Model):
    sender = models.EmailField(max_length=255)
    reciever = models.EmailField(max_length=255)
    subject = models.CharField(max_length=140)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.sender

