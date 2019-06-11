from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title 		= models.CharField(max_length=100)
	content 	= models.TextField()
	date_posted	= models.DateTimeField(default=timezone.now)
	## on_delete -- when the user is deleted
	## CASCADE -- delete the objects that have references to user
	## PROTECT -- forbid the deletion of referenced objects
	## SET_NULL -- set references to NULL
	## SET_DEFAULT -- set the SQL default value
	## SET(...) -- set a given value
	## DO_NOTHING -- 
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post-detail", kwargs={"pk": self.pk})