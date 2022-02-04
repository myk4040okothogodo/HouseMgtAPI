from django.db import models

from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` wit an emaill, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_paassword(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser(admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password')
        if email is None:
            raise TypeError('Superusers must have an email')
        if username is None:
            raise TypeError('Superusers must have a username.')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using= self._db)

        return user




class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False) # validators should be a list

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    phone = models.OneToOneField(PhoneNumber, on_delete=models.CASCADE)
    #room = models.ForeignKey(Room, unique=True, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default = timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone']


    objects = UserManager()

    def __str__(self):
        return f"{self.username}"
