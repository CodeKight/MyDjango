from django.urls import path 
from .views import first, home, contact_us

urlpatterns=[
    path('first/', first),
    path('home/', home),
    path('contact_us/', contact_us),
]