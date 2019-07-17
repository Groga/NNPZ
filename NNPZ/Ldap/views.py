from django.shortcuts import render


# Create your views here.

# создание подключение к LDAP (AD)
def Ldap_connect(request):

    return render(request, 'Ldap/ldap_connect.html')