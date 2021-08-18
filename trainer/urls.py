from django.urls import path
from .views import register_trainer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/',register_trainer,name='register_trainer'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
