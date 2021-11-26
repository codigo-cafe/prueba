from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class ClientManager(BaseUserManager):
    def _create_client(self, username, ci, name, last_name, password, is_staff, is_superuser, **extra_fields):
        client = self.model(
            username = username,
            ci = ci,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        client.set_password(password)
        client.save(using=self.db)
        return client

    def create_client(self, username, ci, name, last_name, password=None, **extra_fields):
        return self._create_client(username, ci, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, ci, name, last_name, password=None, **extra_fields):
        return self._create_client(username, ci, name, last_name, password, True, True, **extra_fields)

class Client(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    ci = models.CharField('Cédula de Identidad' ,max_length = 10, unique = True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = ClientManager()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['ci','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'