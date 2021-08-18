from django.urls import path
from .views import register_events
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/',register_events,name='register_events'),
]
