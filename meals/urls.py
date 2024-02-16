from django.urls import path
from . import api

#   meal/
urlpatterns = [
    path('list/', api.MealMixinAPI.as_view()),
]