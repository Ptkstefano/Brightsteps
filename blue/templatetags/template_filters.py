
from django import template
from datetime import date

from django.shortcuts import get_object_or_404
from blue.models import Profissional, Endereco, Responsavel, Paciente, Checklist

register = template.Library()


@register.filter
def get(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

@register.filter
def get_level(name):
    return name.split('_')[0]

@register.filter
def get_competencia(name):
    if len(name.split('_')) != 3:
        return
    return name.split('_')[1]

@register.filter
def get_number(name):
    if len(name.split('_')) != 3:
        return
    return name.split('_')[2]

@register.filter
def get_responsaveis(pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    obj_responsaveis = paciente.responsavel.all()
    lista_nomes_responsaveis = []
    for responsavel in obj_responsaveis:
        lista_nomes_responsaveis.append(responsavel.nome + ' ' + responsavel.sobrenome)
    return lista_nomes_responsaveis

@register.filter
def get_responsavel(pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    responsavel = paciente.responsavel
    return responsavel.nome

@register.filter
def get_attribute(obj, attr):
    if hasattr(obj, attr):
        return getattr(obj, attr)
    else:
        return None