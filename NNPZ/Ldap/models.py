from django.db import models


# Create your models here.

''' 
  Класс для подключения к серверу ldap, содержит имя пользователя,
дату его создания (изменения, удаления), последнего подключения
 '''
class Ldap_user():
    User_name = models.CharField(max_length=50)
    #Passwd_user = models.CharField()
    Date_create_user = models.DateField(auto_now_add=True)
    Date_upgrade_user = models.DateField(auto_now_add=True)
    Date_delite_user=models.DateField(auto_now_add=True)
    Date_upgrade_connect=models.DateField(auto_now_add=True)
    #pass

'''
  Класс настроек подключения к серверу(имя, ип адреса, даты)
'''
class Ldap_server():
    Server1 = models.CharField(max_length=50)
    Server2 = models.CharField(max_length=50)
    ip_server1 = models.IPAddressField()
    ip_server2 = models.IPAddressField()
    Date_create_server1 = models.DateField(auto_now_add=True)
    Date_create_server2 = models.DateField(auto_now_add=True)
    #pass


'''
  Kласс для хранения групп из ldap
'''
class Ldap_groups():
    Description_groups = models.CharField()
    email_groups = models.EmailField()
    #Group_members = ссылки на полльзователей
    data_create = models.DateTimeField()
    date_upload = models.DateTimeField()
    Name_group = models.CharField()
    Title_group = models.CharField()
    #pass

'''
  Kласс для хранения данных пользователей из ldap
'''
class Ldap_members():
    Name = models.CharField()
    Surname = models.CharField()
    Cabinet = models.CharField()
    Description = models.CharField()
    Phone_number_work1 = models.CharField()
    Phone_number_work2 = models.CharField()
    Phone_number_home1 = models.CharField()
    Phone_number_home2 = models.CharField()
    Phone_number_home3 = models.CharField()
    email = models.EmailField()
    Position = models.CharField()
    Department = models.CharField()
    #pass