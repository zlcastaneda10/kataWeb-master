# coding=utf-8
from __future__ import unicode_literals

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class TiposDeServicio(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='services')

    def __str__(self):
        return self.nombre


class Trabajador(models.Model):
    nombre = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)
    aniosExperiencia = models.IntegerField()
    tiposDeServicio = models.ForeignKey(TiposDeServicio, null=True, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=1000)
    correo = models.CharField(max_length=1000)
    #imagen = models.ImageField(upload_to='images',null=True)
    usuarioId = models.OneToOneField(User, null=True, related_name='trabajador', on_delete=models.CASCADE)


class Comentario(models.Model):
    texto = models.CharField(max_length=1000)
    trabajador = models.ForeignKey(Trabajador, null=True, on_delete=models.CASCADE)
    correo = models.CharField(max_length=1000)


class TrabajadorForm(ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus nombres'})
    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'})
    )
    aniosExperiencia = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de años de experiencia'}),
        label='Años De Experiencia'
    )
    tiposDeServicio = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TiposDeServicio.objects.all(),
        empty_label='Seleccione el tipo de servicio que ofrecerá',
        label='Tipo De Servicio'
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número telefónico'}),
        label='Teléfono'
    )
    correo = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        label='Correo'
    )

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellidos', 'aniosExperiencia', 'tiposDeServicio', 'telefono', 'correo']


class UserForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'password']