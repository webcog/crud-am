from django.urls import path
from core.views import index, about, view_student, updatestudent, delete_student

urlpatterns = [
   path("", index, name="index"),
   path("about/", about, name="about"),
   path("view-student/", view_student, name="view"),
   path("update-student/<int:id>/", updatestudent, name="update"),
   path("delete-student/<int:id>/", delete_student, name="delete")

]