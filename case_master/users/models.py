from django.db import models
from django.contrib.auth.models import BaseUserManager as BUM, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class BaseUserManager(BUM):

    def create_user(self, email, is_active=True, is_admin=True, password=None):
        if not email:
            raise ValueError('用户必须填写邮箱地址')

        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)
        if password is not None:
            user.get_password(password)
        else:
            user.set_unusable_password()
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, is_active=True, is_admin=True, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class BaseUser(BaseUserManager, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='邮件地址',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    object = BaseUserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
