from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new/", views.create_entry, name="new_entry"),
    path("random/", views.random_entry, name="random_entry")
]
