from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_alloc, name="project_alloc"),
    path("", views.upload_file_view, name="upload_file_view"),
]