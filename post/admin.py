from django.contrib import admin
from post.models import Categories
from post.models import Post

admin.site.register(Post)
admin.site.register(Categories)
