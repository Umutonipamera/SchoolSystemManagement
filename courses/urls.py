from django.urls import path
from .views import register_courses,courses_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/',register_courses,name='register_courses'),
    path('list/',courses_list,name="courses_list"),
]
