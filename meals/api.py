from django.shortcuts import render
from rest_framework import generics,mixins

from .models import Meal
from .serializers import MealSerializer

class MealMixinAPI(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
