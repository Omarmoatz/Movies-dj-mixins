from django.shortcuts import render
from rest_framework import generics,mixins

from .models import Meal
from .serializers import MealSerializer

class MealMixinAPI(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   generics.GenericAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
