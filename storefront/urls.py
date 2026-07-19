from django.urls import path
from . import views

app_name = "storefront"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("book/<slug:slug>/", views.book_detail, name="book_detail"),
    path("about/", views.about, name="about"),
    path("vision/", views.vision, name="vision"),
    path("ebooks/", views.ebooks, name="ebooks"),
    path("contact/", views.contact, name="contact"),
]
