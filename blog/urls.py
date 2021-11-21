from django.urls import path
from .views import posts

urlpatterns = [
    path('Post/',posts, name='home'),
]

