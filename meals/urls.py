from django.urls import path
from . import api

#   meal/
urlpatterns = [
    path('list/', api.MealMixinAPI.as_view()),
    path('<int:pk>/', api.MealMixinAPI.as_view()),
    path('create/', api.MealMixinAPI.as_view()),
    path('<int:pk>/delete/', api.MealMixinAPI.as_view()),
]