from coffeverse.extensions.database import db
from coffeverse import create_app
from coffeverse.models import cliente
from coffeverse.models import categoria_produto
from coffeverse.models import empresa
from coffeverse.models import endereco_entrega
from coffeverse.models import itens_pedidos
from coffeverse.models import motoboy
from coffeverse.models import pedido
from coffeverse.models import produto

app = create_app()
with app.app_context():
    db.create_all()