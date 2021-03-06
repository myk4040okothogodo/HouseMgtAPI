from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from ..building.models import Building
from ..house.models import House

class UserManager(BaseUserManager):
    def create_user(self, username, email,phone_number, password=None, **kwargs):
        """Create and return a `User` wit an emaill, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email')
        if phone_number is None:
            raise TypeError('Users must have a phone number')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username,email, phone_number, password):
        """
        Create and return a `User` with superuser(admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password')
        if email is None:
            raise TypeError('Superusers must have an email')
        if phone_number is None:
            raise TypeError('Superusers must have a phone number')
        if username is None:
            raise TypeError('Superusers must have a username.')
        user = self.create_user(username, email,phone_number, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using= self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(default = "+************")
    date_joined = models.DateTimeField(default = timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number']


    objects = UserManager()

    def __str__(self):
        return f"{self.username}"
