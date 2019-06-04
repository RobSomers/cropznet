from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("brokemon", views.brokemon, name="brokemon"),
	path("brokemon/<str:name>", views.brokemon, name="brokemonpages"),
]