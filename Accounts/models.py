from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, rol,password=None):
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have a email")
        if not rol:
            raise ValueError("Users must have a rol")
        if('alumno' == rol):
            print('Creando alumno')
        if('profe'== rol):
            print('creando profe')
        else:
            user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            rol=rol
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password,rol):
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have a email")
        if not rol:
            raise ValueError("Users must have a rol")
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            rol=rol

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email',max_length=100, unique=True)
    rol = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=13,default='0000000000')
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password','rol']
    # add additional fields in here

    def __str__(self):
        return self.first_name +' '+ self.last_name +' '+self.rol
