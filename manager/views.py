from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from . import models
from . import serializers

# class Home(ListCreateAPIView):
#     def get_queryset(self):
#         print (f'{self.kwargs}\n\n\n')
#         return models.Category.objects.select_related('user').all()
#     serializer_class = serializers.CategorySerializer

class Home(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer