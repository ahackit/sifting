from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeListSerializer, RecipeSerializer

# Create your views here.


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecipeSerializer(instance)
        return Response(serializer.data)
