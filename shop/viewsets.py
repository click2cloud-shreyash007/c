from rest_framework import viewsets
from . import models
from . import serializers

class itemViewset(viewsets.ModelViewSet):
    queryset = models.item.objects.all()
    serializer_class = serializers.itemSerializer