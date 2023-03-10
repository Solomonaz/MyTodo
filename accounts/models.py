from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, username,password=None):
        if not email:
            raise ValueError('Email must be provided!') 
        if not username:
            raise ValueError('User ust have user name!')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user =self.create_user(
            email  =self.normalize_email(email),
            password =password,
            username =username,
        )
        user.is_admin =True
        user.is_active =True
        user.is_staff =True
        user.is_superadmin =True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=50, unique= True)
    email    = models.EmailField(max_length=50, unique=True)

        # required fields

    date_joined     =models.DateField(auto_now_add=True)
    last_login      =models.DateField(auto_now_add=True)
    is_admin        =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=True)
    is_active        =models.BooleanField(default=True)
    is_superadmin        =models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects =AccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


