from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from pprint import pprint
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categories.models import Category, PokemonMap
from categories.serializers import PokemonSerializer, CategorySerializer

class CategoryView(APIView):

    def get_object(self, cid):
        try:
            return Category.objects.get(cid=cid)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cid):
        category = self.get_object(cid)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PokemonMapView(APIView):
    def get_object(self, pid):
        try:
            return PokemonMap.objects.get(cid=pid)
        except PokemonMap.DoesNotExist:
            raise Http404
    def get(self, request, pid):
        pokemon = self.get_object(pid)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    def post(self, request):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response(status=status.HTTP_409_CONFLICT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def editpokemon(self, data):
        pokemap = self.get_object(data['cid'])
        serializer = PokemonSerializer(pokemap, data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return True
        return False

    def put(self, request):
        data = request.data
        for onerow in data:
            resp = self.editpokemon(onerow)
            if not resp:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_202_ACCEPTED)


