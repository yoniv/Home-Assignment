from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Serializes a Message object"""
    class Meta:
        model = Message
        fields = ('sender', 'reciever', 'subject', 'message', 'creation_date', 'is_read')