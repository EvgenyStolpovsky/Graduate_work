from rest_framework import viewsets

from main.models import Modul
from main.serliazers.modul import ModulSerializer


class ModulViewSet(viewsets.ModelViewSet):
    """
    Описание ViewSet для работы с сериализатором ModulSerializer.
    """

    serializer_class = ModulSerializer
    queryset = Modul.objects.all()
