from rest_framework import serializers
from restoration.apps.furniture.models import Legs, Tables, Feet


class LegsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Legs
        fields = '__all__'


class FeetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feet
        fields = '__all__'


class TablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tables
        fields = '__all__'

    def to_representation(self, instance):
        data = super(TablesSerializer, self).to_representation(instance)
        data['leg_id'] = data.pop('legs')
        data['feet_id'] = data.pop('feet')
        return data
