from coffeverse.extensions.database import db
from coffeverse import create_app
from coffeverse.models import cliente
from coffeverse.models import pedido
from coffeverse.models import itens_pedidos

app = create_app()
with app.app_context():
    db.create_all()