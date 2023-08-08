"""aut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blue import views

urlpatterns = [
    path('', views.index),
    path('login_prof', views.login_prof),
    path('registro_prof', views.registro_prof),
    path('registro_paci', views.registro_paci),
    path('edit_paci', views.edit_paci),
    path('save_edit_paci', views.save_edit_paci),
    path('edit_profi', views.edit_profi),
    path('save_edit_profi', views.save_edit_profi),
    path('main', views.main),
    path('logout', views.logout_view),
    path('checklist_find', views.checklist_find),
    path('checklist/<str:paciente_cod>', views.checklist),
    path('checklist/historico/<str:paciente_cod>', views.checklist_historico),
    path('checklist_edit/<int:paciente_id>', views.checklist_edit),
    path('checklist_ajax', views.checklist_ajax),
    path('gerencia', views.gerencia),
    path('gerencia/change', views.change),
    path('gerencia/add', views.add),
    path('gerencia/remove', views.remove),
    path('mudarsenha', views.mudar_senha),
    path('admin/admin', admin.site.urls),
    path('backup', views.backup)
]
