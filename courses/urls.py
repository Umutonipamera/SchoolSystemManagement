
from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from.views import course_list, register_courses,edit_course,delete_course

urlpatterns = [
    path("register/", register_courses, name="register_courses"),
    path("list/", course_list, name="course_list"),
    path("edit/<int:id>/", edit_course, name="edit_course"),
    path("delete/<int:id>/", delete_course, name="delete_course"),
]
