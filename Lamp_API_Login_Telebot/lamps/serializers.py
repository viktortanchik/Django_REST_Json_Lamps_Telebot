from rest_framework import serializers
from .models import Lamps, ProgramLamps1


class LampslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamps
        fields = ('id', 'status', 'mode', 'red', 'green', 'blue')


class LampsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamps
        fields = '__all__'


class ProgramLamps1listSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramLamps1
        fields = ('pixel_1_red', 'pixel_1_green', 'pixel_1_blue')


class ProgramLamps1DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramLamps1
        fields = '__all__'

