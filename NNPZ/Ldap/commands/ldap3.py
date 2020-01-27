from django.core.management.base import BaseCommand
from ldap3 import Server, Connection, ALL

class Command(BaseCommand):


    def add_arguments(self, parser):
        # Указываем сколько и каких аргументов принимает команда.
        # В данном случае, это один аргумент типа str.
        parser.add_argument('AD', nargs=1, type=str)

    def handle(self, *args):

        server = Server('AD')
        conn = Connection(server)
        conn.bind()
