from rest_framework import serializers
from categories.models import Category, PokemonMap

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMap
        fields = ['cid', 'pokeid', 'category', 'current_rank', 'old_rank']

class CategorySerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['cid', 'name', 'pokemon']
