from rest_framework import serializers
from shop.models import Fruit,Vegetable,BestSell

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = '__all__'


class BestSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSell
        fields = '__all__'