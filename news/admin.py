from django.contrib import admin
from news.models import User, Post, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
