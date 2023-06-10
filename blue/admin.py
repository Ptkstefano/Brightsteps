from django.contrib import admin
from .models import Paciente, Checklist, Responsavel, Profissional, Endereco

admin.site.register(Paciente)
admin.site.register(Profissional)
admin.site.register(Checklist)
admin.site.register(Responsavel)
admin.site.register(Endereco)

