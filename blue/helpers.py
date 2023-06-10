import random
from django.utils import timezone
from datetime import datetime
from blue.models import Profissional, Endereco, Responsavel, Paciente, Checklist
from blue.templatetags import template_filters

def create_username(name, surname):
    username = str(name)+str(surname)
    return username

def create_password(name):
    password = name
    return password

def create_date(date):
    date_formated = datetime.strptime(date, '%Y-%m-%d')
    return date_formated

def create_codigo(first_name, last_name):
    codigo = first_name.split(' ')[0] + last_name.split(' ')[0] + str(random.randint(1000, 9999))
    return codigo

def make_score(checklist, level):
    
    checklist_fields = checklist._meta.get_fields()
    score = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    competencia_dict = {
        'cre': 0,
        'cex': 1,
        'cac': 2,
        'cso': 3,
        'imi': 4,
        'cog': 5,
        'jog': 6,
        'mfi': 7,
        'mgr': 8,
        'com': 9,
        'ipe': 10
    }


    for field in checklist_fields:
        if field.name == 'id':
            continue
        if template_filters.get_level(field.name) == level:
            if template_filters.get_competencia(field.name) in competencia_dict:
                if field.value_from_object(checklist) == 3:
                    score[competencia_dict[template_filters.get_competencia(field.name)]] += 1
                elif field.value_from_object(checklist) == 2:
                    score[competencia_dict[template_filters.get_competencia(field.name)]] += 0.5

    if level == 'nv1':
        multiplier = [6.7, 7.15, 0, 10, 25, 25, 12.5, 8.4, 12.5, 20, 5.6]
    elif level == 'nv2':
        multiplier = [10, 8.4, 12.5, 5, 11.2, 12.5, 12.5, 7.15, 14.3, 0, 3.9]
    elif level == 'nv3':
        multiplier = [8.4, 5.6, 0, 6.7, 0, 10, 16.7, 9.1, 12.5, 0, 5.3]
    elif level == 'nv4':
        multiplier = [5.3, 3.4, 0, 11.2, 0, 8.4, 11.2, 5.3, 11.2, 0, 5.6]

    for i in range(0, 11):
        score[i] = score[i]*multiplier[i]
        if score[i] > 100:
            score[i] = 100

    #remove elements not present in level
    if level == 'nv1':
        score.pop(2)
    if level == 'nv2':
        score.pop(9)
    elif level == 'nv3':
        score.pop(9)
        score.pop(4)
        score.pop(2)
    elif level == 'nv4':
        score.pop(9)
        score.pop(4)
        score.pop(2)

    return score

def make_total_score(checklist):
    checklist_fields = checklist._meta.get_fields()

    score = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    competencia_dict = {
        'cre': 0,
        'cex': 1,
        'cac': 2,
        'cso': 3,
        'imi': 4,
        'cog': 5,
        'jog': 6,
        'mfi': 7,
        'mgr': 8,
        'com': 9,
        'ipe': 10
    }

    for field in checklist_fields:
            if template_filters.get_competencia(field.name) in competencia_dict:
                if field.value_from_object(checklist) == 3:
                    score[competencia_dict[template_filters.get_competencia(field.name)]] += 1
                elif field.value_from_object(checklist) == 2:
                        score[competencia_dict[template_filters.get_competencia(field.name)]] += 0.5

    multiplier = [1.75, 1.4, 12.5, 1.86, 7.7, 3, 3.3, 1.8, 3.15, 20, 1.25]

    for i in range(0, 11):
        score[i] = score[i]*multiplier[i]
        if score[i] > 100:
            score[i] = 100
    return score

def fill_checklist(checklist, level):
    checklist_fields = checklist._meta.get_fields()
    for field in checklist_fields:
        if template_filters.get_level(field.name) == level:
            setattr(checklist, field.name, 3)
    return checklist