from django.contrib import admin
from .models import Post

# this make us to add, delete and edit our model
admin.site.register(Post)