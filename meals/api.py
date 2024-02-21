from django.shortcuts import render
from rest_framework import generics,mixins,permissions,authentication

from .models import Meal
from .serializers import MealSerializer
from .permissions import IsStaffEditorPermission

class MealMixinAPI(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication]
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')

        if description is None:
            description = "test perform create"

        serializer.save(description=description)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        description = serializer.validated_data['description']
        name = serializer.validated_data['name']

        if description == None:
            description = "test perform update"

        serializer.save(description=description)
        

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        