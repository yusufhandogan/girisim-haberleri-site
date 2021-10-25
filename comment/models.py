from django.db import models
from django.db import models
from django.utils import timezone
from django.conf import settings
from post.models import Post


class CommentModel(models.Model):

      id = models.AutoField(primary_key=True)
      user = models.ForeignKey(
          settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      post = models.ForeignKey(
          Post, on_delete=models.CASCADE, related_name='post')
      content = models.TextField()
      parent = models.ForeignKey(
          'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
      date = models.DateTimeField(editable=False)

      class Meta:
        ordering = ('date', )

      def __str__(self):
            return self.post.title 

      def save(self, *args, **kwargs):
            if not self.id:
                  self.date = timezone.now()
            self.modified = timezone.now()
            return super(CommentModel, self).save(*args, **kwargs)

      def children(self):
            return CommentModel.objects.filter(parent=self)

      @property
      def any_children(self):
            return CommentModel.objects.filter(parent = self).exists()
      

