from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]