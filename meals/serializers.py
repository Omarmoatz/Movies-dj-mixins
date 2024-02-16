from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Meal
        fields = ['id','name','description','price','category',
                  'preperation_time','image','people','price_after_sale']