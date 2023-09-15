from rest_framework import serializers

from main.models import Modul


class ModulSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modul
        fields = '__all__'
