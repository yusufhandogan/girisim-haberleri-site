from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/post/",include("post.api.urls", namespace = "post")),
    path("api/categories/", include("post.api.urls", namespace = "categories") ),
    path("api/author/", include("author.api.urls", namespace = "author"))
]   + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


