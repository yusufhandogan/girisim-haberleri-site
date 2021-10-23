from django.db import models
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from .utils import get_read_time
from django.conf import settings
from django.utils import timezone
from markdown_deux import markdown
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
import uuid



class Category_Choices(models.TextChoices):
    BİLİNMEYENLER = '13İlinmeyenler'
    KİŞİSEL_GELİŞİM = 'Kişisel Gelişim'
    İLHAM_AL = 'İlham Al'
    YATIRIM_HABERLERİ = 'Yatırım Haberleri'
    GİRİŞİMCİLİK = 'Girişimcilik'
    ENGLİSH_NEWS = 'English News'
    BAŞARI_HİKAYELERİ = "Başarı Hikayeleri"




class Color_Choices(models.TextChoices):
    INDIGO = 'indigo'
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    BLUE = 'blue'
    GRAY = 'gray'
    PINK = "pink"





class Categories(models.Model):

    name = models.CharField(max_length=50,choices=Category_Choices.choices,default=Category_Choices.BİLİNMEYENLER)
    color = models.CharField(max_length=30,choices=Color_Choices.choices, default=Color_Choices.RED)
    href = models.SlugField(editable=False,unique=True)
    thumbnail = models.ImageField(upload_to="postpost",null=True,blank=True)

    def __str__(self):
        return self.name

    def get_category_slug(self):
        slug = slugify(self.name.replace("ı","i"))
        unique = slug
        number = 1

        while Categories.objects.filter(slug=unique).exists():
            unique = "{}-{}" .format(slug,number)
            number += 1

        return unique
    def save(self, *args, **kwargs):
        self.href = slugify(self.name)
        super(Categories,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.href

class Post(models.Model):

    authorId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255)
    categoryID = models.ManyToManyField(Categories,)
    content = models.TextField(blank=False)
    href = models.SlugField(editable=False,unique=True)
    draft = models.BooleanField(default=True)
    readingtime = models.IntegerField(default=0)
    updated = models.DateTimeField()
    date = models.DateTimeField(editable=False,null=True)
    published = models.DateField(default=timezone.now)
    featuredimage = models.ImageField(null=True, blank=True, upload_to='post')




    class Meta:
        ordering = ['-date', '-updated']

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        unique = slug
        number = 1

        while Post.objects.filter(slug=unique).exists():
            unique = "{}-{}" .format(slug,number)
            number += 1

        return unique
    #@property
    #def comments(self):
    #    instance = self
    #    qs = Comment.objects.filter_by_instance(instance)
    #    return qs


    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.href and instance.title:
        if not Post.objects.filter(href=slugify(instance.title)).exists():
            instance.href = slugify(instance.title)
        else:
            instance.href = slugify(instance.title) + str(uuid.uuid4())[:8]





pre_save.connect(pre_save_receiver, sender=Post)




