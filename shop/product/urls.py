from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name="all"),
    path('men/', views.all, name="men"),
    path('women/', views.all, name="women"),
    path('children/', views.all, name="children"),
    path('feedback/', views.feedback, name="feedback"),
    path('create/', views.create, name="create"),
    ]