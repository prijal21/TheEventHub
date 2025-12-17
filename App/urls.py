from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mehendi/', views.mehendi, name='mehendi'),
    path('birthday/', views.birthday, name='birthday'),
    path('fruits-catering/', views.fruits_catering, name='fruits_catering'),
    path('salad-dressing/', views.salad_dressing, name='salad_dressing'),
    path('juice-catering/', views.juice_catering, name='juice_catering'),
    path('contact/', views.contact, name='contact'),
]