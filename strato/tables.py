# example/app/tables.py
from models import clients
from table import Table
from table.columns import Column


class ClientTable(Table):
    usuario = Column(field='usuario')
    nombreapp = Column(field='nombreapp')
    ip = Column(field='ip')
    class Meta:
        model = clients
