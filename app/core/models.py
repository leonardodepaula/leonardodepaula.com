# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Manager
from .managers import UserManager

####################
#### User model ####
####################

class User(AbstractUser):

    username = None
    email = models.EmailField(verbose_name='E-Mail', unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = '1. Usuários'

#################
#### Contato ####
#################

class Contato(models.Model):

    nome = models.CharField(max_length=300, blank=False, null=False, verbose_name='Nome')
    email = models.EmailField(verbose_name="E-Mail")
    texto = models.TextField(blank=False, null=False, verbose_name='Mensagem')
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = '2. Contatos'
    
    def __str__(self):
        return f'{str(self.nome)} - {str(self.email)}'