from django.contrib import admin
from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
	## the URL path plus the views
	path("", PostListView.as_view(), name="blog-home"),
	path("about/", views.about, name="blog-about"),
	
]