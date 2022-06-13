from django.urls import path
from . import views


urlpatterns = [
    path('', views.allbooks, name='home'),
    path('addbook/', views.addbook, name='add_book'),
    path('deletebook/<int:id>/', views.deletebook, name='deletebook'),
]
