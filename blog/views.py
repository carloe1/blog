from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


# Home Page
def home(request):
	# return HttpResponse("<h1>Blog Home")
	context = {
		"posts" : Post.objects.order_by("-date_posted")
	}
	return render(request, "blog/home.html", context)

class PostListView(ListView):
	model = Post

	template_name = "blog/home.html" # <app>/<model>_<viewtype>.html
	context_object_name = "posts"
	ordering = ["-date_posted"]


## About Page
def about(request):
	#return HttpResponse("<h1>Blog About</h1>")
	return render(request, "blog/about.html",{"title":"About"})