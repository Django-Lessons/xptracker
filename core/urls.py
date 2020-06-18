from core import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.start, name='start'),
]
