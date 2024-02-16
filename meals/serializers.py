from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Meal
        fields = '__all__'