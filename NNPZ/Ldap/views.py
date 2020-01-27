from django.shortcuts import render



# Create your views here.

# создание подключение к LDAP (AD)
def Ldap_connect(request):

    return render(request, 'Ldap/ldap_connect.html')





from django.shortcuts import render_to_response
from django.template import RequestContext
from .commands.Ldap_logic import *

# Список отделов
departments = [ 'Начальство', 'Отдел продаж', 'Отдел сбыта' ]



def department(request, name):
    context = RequestContext(request)
    context['contacts'] = ldap_getDepartment(name.encode('utf-8'))
    context['departments'] = departments
    context['department'] = name
    return render_to_response('Ldap/ldap.html', context)



