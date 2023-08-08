from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
import blue.forms
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from blue.models import Profissional, Endereco, Responsavel, Paciente, Checklist
from django.contrib.auth.models import User
from django.utils import timezone
from blue import helpers
from blue.templatetags import template_filters
from datetime import datetime, date
import random
from django.forms import modelform_factory
from django.db.models import Q
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    print(timezone.localdate())
    return render(request, 'index.html')

def login_prof(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(main)

    return render(request, 'login_prof.html')

def logout_view(request):
    auth.logout(request)
    return redirect(index)


@login_required(login_url='/login_prof')
def gerencia(request):

    profissional_logado = get_object_or_404(Profissional, user=request.user)
    if profissional_logado.admin == False:
        return redirect(main)
    
    lista_responsaveis = Responsavel.objects.all()
    lista_pacientes = Paciente.objects.all()
    lista_profissionais = Profissional.objects.all()

    return render(request, "paineladm.html", {'lista_responsaveis': lista_responsaveis, 'lista_pacientes': lista_pacientes, 'lista_profissionais': lista_profissionais})


#@login_required(login_url='/login_prof')
def main(request):

    profissional_logado = get_object_or_404(Profissional, user=request.user)

    #if profissional_logado.admin:

    #else:
    lista_pacientes = Paciente.objects.filter(profissional = profissional_logado).filter(active = True)
    lista_responsaveis = Responsavel.objects.filter(Q(id__in=lista_pacientes.values('responsavel')))


    return render(request, "main.html", {'profissional': profissional_logado, 'lista_responsaveis': lista_responsaveis, 'pacientes': lista_pacientes})


def registro_paci(request):
    profissional_logado = get_object_or_404(Profissional, user=request.user)

    if request.method=='POST':

        #REGISTRO PACIENTE
        paciente = Paciente()
        paciente_form = blue.forms.form_registro_paciente(request.POST, instance=paciente)
        if paciente_form.is_valid():
            paciente = paciente_form.save(commit=False)

        paciente.cod_acesso = helpers.create_codigo(paciente.nome, paciente.sobrenome)

        checklist = Checklist()
        checklist.paciente = paciente

        if request.POST.get('nv1_fill'):
            checklist = helpers.fill_checklist(checklist, 'nv1')
        if request.POST.get('nv2_fill'):
            checklist = helpers.fill_checklist(checklist, 'nv2')
        if request.POST.get('nv3_fill'):
            checklist = helpers.fill_checklist(checklist, 'nv3')
        if request.POST.get('nv4_fill'):
            checklist = helpers.fill_checklist(checklist, 'nv4')

        responsavel = Responsavel()
        responsavel_form = blue.forms.form_registro_responsavel(request.POST, instance=responsavel)
        if responsavel_form.is_valid():
            responsavel = responsavel_form.save(commit=False)

        endereco = Endereco()
        endereco_form = blue.forms.form_registro_endereco(request.POST, instance=endereco)
        if endereco_form.is_valid():
            endereco = endereco_form.save(commit=False)

        paciente.data_registro=timezone.now()

        #TRY CATCH
        endereco.save()
        responsavel.save()
        paciente.endereco = endereco
        paciente.responsavel = responsavel
        paciente.save()
        paciente.profissional.add(profissional_logado)
        checklist.save()
    
        return redirect(main)
    else:
        return render(request, 'registro_paci.html', {'form_paci': blue.forms.form_registro_paciente, 'form_resp': blue.forms.form_registro_responsavel, 'form_end': blue.forms.form_registro_endereco, 'resp_formset': blue.forms.form_registro_responsavel})

def edit_profi(request):
    if request.method!='POST':
        return redirect(main)
    profissional = get_object_or_404(Profissional, pk = request.POST.get('pk'))
    endereco = get_object_or_404(Endereco, pk = profissional.endereco.pk)
    return render(request, 'edit_profi.html', {'profissional': profissional, 'endereco': endereco })

def save_edit_profi(request):
    if request.method!='POST':
        return redirect(main)
    
    profissional = get_object_or_404(Profissional, pk = request.POST.get('pk'))
    profissional.nome = request.POST.get('nome')
    profissional.sobrenome = request.POST.get('sobrenome')
    profissional.cpf = request.POST.get('cpf')
    profissional.email = request.POST.get('email')
    profissional.data_nascimento = request.POST.get('data_nascimento')
    profissional.tel_fixo = request.POST.get('tel_fixo')
    profissional.tel_celular = request.POST.get('tel_celular')
    profissional.save()

    endereco = get_object_or_404(Endereco, pk = profissional.endereco.pk)
    endereco.rua = request.POST.get('rua')
    endereco.cep = request.POST.get('cep')
    endereco.cidade = request.POST.get('cidade')
    endereco.estado = request.POST.get('estado')
    endereco.numero = request.POST.get('numero')
    endereco.save()

    return redirect(gerencia)

def edit_paci(request):
    if request.method!='POST':
        return redirect(main)
    paciente = get_object_or_404(Paciente, pk = request.POST.get('pk'))
    responsavel = get_object_or_404(Responsavel, pk = paciente.responsavel.pk)
    endereco = get_object_or_404(Endereco, pk = paciente.endereco.pk)
    return render(request, 'edit_paci.html', {'paciente': paciente, 'responsavel': responsavel, 'endereco': endereco })

def save_edit_paci(request):
    if request.method=='POST':
        paciente = get_object_or_404(Paciente, pk = request.POST.get('pk'))
        paciente.nome =  request.POST.get('nome')
        paciente.sobrenome = request.POST.get('sobrenome')
        paciente.data_nascimento =  request.POST.get('data_nascimento')
        paciente.cpf = request.POST.get('cpf')
        paciente.save()

        responsavel = get_object_or_404(Responsavel, pk = paciente.responsavel.pk)
        responsavel.nome_completo = request.POST.get('nome_completo')
        responsavel.email = request.POST.get('email')
        responsavel.telefone1 = request.POST.get('telefone1')
        responsavel.telefone2 = request.POST.get('telefone2')
        responsavel.relacao = request.POST.get('relacao')
        responsavel.save()

        endereco = get_object_or_404(Endereco, pk = paciente.endereco.pk)
        endereco.rua = request.POST.get('rua')
        endereco.cep = request.POST.get('cep')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        endereco.numero = request.POST.get('numero')
        endereco.save()

        return redirect(main)
    
#@login_required(login_url='/login_prof')
def registro_prof(request):
    ##TODO
    if request.method=='POST':
        profissional = Profissional()
        endereco = Endereco()

        profissional_form = blue.forms.form_registro_responsavel(request.POST, instance=profissional)
        endereco_form = blue.forms.form_registro_endereco(request.POST, instance=endereco)

        endereco = endereco_form.save(commit=False)
        profissional = profissional_form.save(commit=False)

        login_inicial = helpers.create_username(profissional.nome, profissional.sobrenome)
        senha_inicial = helpers.create_password(profissional.nome)

        profissional.login_inicial=login_inicial
        profissional.senha_inicial=senha_inicial

        user = User.objects.create_user(login_inicial, profissional.email, senha_inicial)

        profissional.endereco = endereco
        profissional.user = user

        #TRY CATCH
        user.save()
        endereco.save()
        profissional.save()

        return redirect(main)
        
    return render(request, "registro_prof.html", {'form_profi': blue.forms.form_registro_profissional, 'form_end': blue.forms.form_registro_endereco})

def checklist(request, paciente_cod):
    paciente = get_object_or_404(Paciente, cod_acesso = paciente_cod)
    checklist = Checklist.objects.filter(paciente=paciente.pk).latest('data')
    checklist_fields = checklist._meta.get_fields()
    checklist_fields_copy = list(checklist_fields)

    #checklist_fields_copy.remove('<django.db.models.fields.BigAutoField: id>')
    #checklist_fields_copy.remove('ID')
    #checklist_fields_copy.remove('Data')

    del checklist_fields_copy[2]
    del checklist_fields_copy[0]
    del checklist_fields_copy[0]

    nv1_score = helpers.make_score(checklist, 'nv1')
    nv2_score = helpers.make_score(checklist, 'nv2')
    nv3_score = helpers.make_score(checklist, 'nv3')
    nv4_score = helpers.make_score(checklist, 'nv4')
    total_score = helpers.make_total_score(checklist)

    #1- 10 (cre 15, cex 14, cac 0, cso 10, imi 4, cog 4, jog 8, mfi 12, mgr 8, com 5, ipe 18)
    #2- 9 (cre 10, cex 12, cac 8, cso 20, imi 9, cog 8, jog 8, mfi 14, mgr 7, com 0, ipe 26)
    #3- 8 (cre 14, cex 18, cac 0, cso 15, imi 0, cog 10, jog 6, mfi 11, mgr 8, com 0, ipe 19)
    #4- 8 (cre 19, cex 30, cac 0, cso 9, imi 0, cog 12, jog 9, mfi 19, mgr 9, com 0, ipe 18)

    return render(request, "checklist.html", {'checklist': checklist, 'checklist_fields': checklist_fields_copy, 'paciente': paciente, 'nv1_score': nv1_score, 'nv2_score': nv2_score, 'nv3_score': nv3_score, 'nv4_score': nv4_score, 'total_score': total_score})

def checklist_historico(request, paciente_cod):
    paciente = get_object_or_404(Paciente, cod_acesso=paciente_cod)

    checklists = Checklist.objects.filter(paciente=paciente.pk)
    score_list = []
    for checklist in checklists:
        score = helpers.make_total_score(checklist)
        data = checklist.data
        score_list.append ({'Data': data, 'Score': score})

    score_list.reverse()
    checklist_final = Checklist.objects.filter(paciente=paciente.pk).latest('data')
    total_score = helpers.make_total_score(checklist_final)

    return render(request, 'checklist_historico.html', {'paciente': paciente, 'checklist_final': checklist_final, 'total_score': total_score, 'score_list': score_list})

def checklist_edit(request, paciente_id):
    mensagem = 'Salvar alterações'
    paciente_model = get_object_or_404(Paciente, pk=paciente_id)
    checklist = Checklist.objects.filter(paciente=paciente_id).latest('data')
    if request.method=='POST':
        form = blue.forms.form_checklist(request.POST)
        if form.is_valid():
            form.save()
            mensagem = 'Alterações salvas'
        else:
            print(form.errors)
    else:
        form=blue.forms.form_checklist(instance=checklist)

    return render(request, "checklist_edit.html", {'checklist_form': form, 'descriptions': blue.forms.description_dict, 'paciente': paciente_model, 'mensagem': mensagem})

def checklist_ajax(request):
    
    if request.method == 'POST': 
        id = request.POST.get('id') 
        name = request.POST.get('name')
        value = request.POST.get('value')

        checklist = Checklist.objects.filter(paciente=id).latest('data')
        if checklist.data.date() == timezone.now().date():
            setattr(checklist, name, value)
            checklist.save()
        else:
            checklist.pk = None
            setattr(checklist, name, value)
            checklist.save()

    return JsonResponse({"status": 'Success'}) 

@login_required(login_url='/login_prof')
def remove(request):

    profissional_logado = get_object_or_404(Profissional, user=request.user)
    if profissional_logado.admin == False:
        return redirect(main)

    paciente_pk = request.GET.get('pk')
    profissional_pk = request.GET.get('profi_pk')

    paciente = get_object_or_404(Paciente, id=paciente_pk)
    profissional = get_object_or_404(Profissional, id=profissional_pk)

    paciente.profissional.remove(profissional)
    paciente.save()

    return redirect(gerencia)

@login_required(login_url='/login_prof')
def change(request):

    profissional_logado = get_object_or_404(Profissional, user=request.user)
    if profissional_logado.admin == False:
        return redirect(main)

    model = request.GET.get('model')
    id = request.GET.get('pk')

    if model == 'paciente':
        paciente = get_object_or_404(Paciente, id=id)
        if paciente.active:
            paciente.active = False
        else:
            paciente.active = True

        paciente.save()

    if model == 'profissional':
        profissional = get_object_or_404(Profissional, id=id)
        if profissional.active:
            profissional.active = False
        else:
            profissional.active = True

        profissional.save()
    
    return redirect(gerencia)

def mudar_senha(request):
    if request.method=='GET':
        return render(request, "mudarsenha.html")
    if request.method=='POST':
        senha_atual = request.POST.get('senha_atual')
        senha_1 = request.POST.get('nova_senha_1')
        senha_2 = request.POST.get('nova_senha_2')

        user = request.user

        if user.check_password(senha_atual) and senha_1 == senha_2:
            user.set_password(senha_1)
            user.save()
        else:
            return redirect(mudar_senha)

        return redirect(main)

@login_required(login_url='/login_prof')
def add(request):

    profissional_logado = get_object_or_404(Profissional, user=request.user)
    if profissional_logado.admin == False:
        return redirect(main)
    
    paciente = get_object_or_404(Paciente, id = request.GET.get('paciente'))
    profissional = get_object_or_404(Profissional, id = request.GET.get('profissional'))
    paciente.profissional.add(profissional)
    
    return redirect(gerencia)

def checklist_find(request):
    paciente = Paciente.objects.get(cod_acesso=request.POST.get('codigo'))
    if paciente != None:
        return redirect(checklist, paciente_cod=paciente.cod_acesso)
    else:
        return redirect(index)

@login_required(login_url='/login_prof')
def backup(request):
    profissional_logado = get_object_or_404(Profissional, user=request.user)
    if profissional_logado.admin == False:
        return redirect(main)
    else:
        file_path = os.path.join(BASE_DIR, 'db.sqlite3')
        response = FileResponse(open(file_path, 'rb'))
        return response
