from rest_framework import serializers
from. import models

class UDserializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetails
        fields = "__all__"