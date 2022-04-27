from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.forms import CharField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, password, **kwargs):
        """
        Creates and saves a User with the given email,
        name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have an name')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **kwargs,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            **kwargs
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Advertiser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    uid = models.CharField(max_length=255, unique=True)
    phone_number = CharField(max_length=15)
    address = CharField( max_length=255)
    name = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin