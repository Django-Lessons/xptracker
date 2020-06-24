from core import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('expense', views.expense, name='expense'),
    path('start', views.start, name='start'),
    path('accounts', views.accounts, name='accounts'),
]
