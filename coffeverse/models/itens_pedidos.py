from coffeverse.extensions.database import db
class ItensDoPedido(db.Model):
    __tablename__ = 'tb_itens_do_pedido'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('tb_pedido.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('tb_produto.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    pedido = db.relationship('Pedido', back_populates='itens')
    produto = db.relationship('Produto', back_populates='itens')

    def to_dict(self):
        return {
            'id': self.id,
            'pedido_id': self.pedido_id,
            'produto_id': self.produto_id,
            'quantidade': self.quantidade,
            'preco_unitario': float(self.preco_unitario),
            'produto': self.produto.to_dict()  # caso queira retornar detalhes do produto
        }
