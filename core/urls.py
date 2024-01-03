from django.urls import path
from core.views import index, about, view_student

urlpatterns = [
   path("", index, name="index"),
   path("about/", about, name="about"),
   path("view-student/", view_student, name="view")
]