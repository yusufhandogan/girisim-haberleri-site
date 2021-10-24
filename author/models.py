from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import slugify


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError("Kullanıcı Mail Adresi Olmalı")

        if not username:
            raise ValueError("Kullanıcı adı zorunlu")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=60)
    displayName = models.CharField(max_length=120, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    bgImage = models.ImageField(upload_to="background", null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    desc = models.TextField(blank=True, null=True)
    jobName = models.CharField(max_length=20, default="Author Job")
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.displayName)

        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
