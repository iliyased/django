from django.urls import path
from .views import home
from .views import name

urlpatterns = [
    path('home/',home),
    path('name/',name),

]

