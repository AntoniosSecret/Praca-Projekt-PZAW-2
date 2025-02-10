from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post

admin.site.unregister(Group)

admin.site.register(Post)

# Register your models here.
