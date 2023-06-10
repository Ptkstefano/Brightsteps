from django.forms import ModelForm, RadioSelect
from django import forms
from blue.descriptions import description_dict
import blue.models

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 

class form_registro_profissional(ModelForm):
    class Meta:
        model = blue.models.Profissional
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'data_nascimento', 'tel_fixo', 'tel_celular']

class form_registro_paciente(ModelForm):
    class Meta:
        model = blue.models.Paciente
        fields = ['nome', 'sobrenome', 'data_nascimento', 'cpf']

class form_registro_responsavel(ModelForm):
    class Meta:
        model = blue.models.Responsavel
        fields = ['nome_completo', 'relacao', 'email', 'telefone1', 'telefone2']

class form_registro_endereco(ModelForm):
    class Meta:
        model = blue.models.Endereco
        fields = ['cidade', 'estado', 'cep', 'numero', 'rua']

widgets = {}

class form_checklist(ModelForm):

    widget_fields = []

    for key in description_dict.keys():
        widget_fields.append(key)

    for field in widget_fields:
        widgets[field] = RadioSelect

    class Meta:
        model = blue.models.Checklist
        fields = '__all__'
        widgets = widgets
