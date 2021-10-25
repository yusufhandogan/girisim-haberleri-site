from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from markdown_deux import markdown
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
import uuid
from post.models import Categories


class PostAudio(models.Model):

    authorId = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    audioUrl = models.URLField(null=False, blank=False)
    desc = models.CharField(max_length=255)
    categoriesId = models.ManyToManyField(Categories)
    content = models.TextField(blank=False)
    href = models.SlugField(editable=False, unique=True)
    draft = models.BooleanField(default=True)
    readingTime = models.IntegerField(default=0)
    updated = models.DateTimeField()
    date = models.DateTimeField(editable=False, null=True)
    published = models.DateField(default=timezone.now)
    featuredimage = models.ImageField(
        null=True, blank=True, upload_to='post_audio')

    def save(self, *args, **kwargs):
        if not self.id:
            self.href = slugify(self.title)

        super(PostAudio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
