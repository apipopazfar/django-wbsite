from django.db import models
from django.utils import timezone

# define model and it object Post(models.model)
# always start a class name with upercase
class Post(models.Model):

	# variable= DataType/Properties (limit)
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(
		default=timezone.now)
	published_date=models.DateTimeField(
		blank=True, null=True)

	# define function
	# lowercase, can use underscore
	# (self) python sensitive to whitespace, 
	# need to indent method inside the class
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	# this to return something
	# for this one we return post title
	# __str__ define string text
	def __str__(self):
		return self.title