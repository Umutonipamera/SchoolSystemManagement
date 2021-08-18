from django.urls import path
from .views import register_student,student_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/',register_student,name='register_student'),
    path('list/',student_list,name="student_list"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



   

