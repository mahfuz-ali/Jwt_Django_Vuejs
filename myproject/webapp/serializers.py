from rest_framework import serializers
from . models import employees, JWTPayloadTrack


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__'


class JWTPayloadTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JWTPayloadTrack
        fields = '__all__'