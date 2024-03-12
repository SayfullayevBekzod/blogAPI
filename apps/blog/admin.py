from django.contrib import admin

from apps.blog.models import Like, User, Post, Comment

admin.site.register([Like, User, Post, Comment])
