from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extera_fields):
        if not email:
            raise ValueError(_('please enter email'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extera_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extera_fields):
        extera_fields.setdefault('is_staff', True)
        extera_fields.setdefault('is_superuser', True)
        extera_fields.setdefault('is_active', True)

        if extera_fields.get('is_staff') is not True:
            raise ValueError (_('superuser must have is_staff=True'))
        if extera_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser=True'))
        
        return self.create_user(email,password,**extera_fields)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email