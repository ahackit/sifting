from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Recipe, UOM
from .serializers import RecipeListSerializer, RecipeSerializer, UOMSerializer

# Create your views here.


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecipeSerializer(instance)
        return Response(serializer.data)


class UOMViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer
