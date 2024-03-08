from django.urls import path
from django.views.generic import RedirectView
from .views import index

urlpatterns = [
    path("", RedirectView.as_view(url='home/')),
    path("home/", index),
    path("contact/", index),
    path("blog/", index),
]