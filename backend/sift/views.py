from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Recipe, UOM
from .serializers import RecipeListSerializer, RecipeSerializer, UOMSerializer, RecipeGroceryListSerializer

# Create your views here.


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecipeSerializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def grocerylist(self, request, pk=None):
        recipe = Recipe.objects.get(id=pk)

        serializer = RecipeGroceryListSerializer(recipe)
        return Response(serializer.data)


class UOMViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer

    @action(detail=False, methods=['get'])
    def convert(self, request, pk=None):
        start_uom_number = self.request.GET['start_uom_number']
        start_uom_txt = self.request.GET['start_uom']
        end_uom_txt = self.request.GET['end_uom']

        start_uom = UOM.objects.get(measurement=start_uom_txt)

        results = start_uom.convert_to(start_uom_number, end_uom_txt)
        return Response(results)
