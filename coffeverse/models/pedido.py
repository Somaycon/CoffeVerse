from coffeverse.extensions.database import db

class Pedido(db.Model):
    __tablename__ = "tb_pedido"
    id = db.Column(db.Integer, primary_key = True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('tb_cliente.id'), nullable = False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_enderecos_de_entrega.id'), nullable = False)
    data = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    
    cliente = db.relationship('Cliente', back_populates='pedidos')
    endereco = db.relationship('EnderecoDeEntrega', back_populates='pedidos')

    def to_dict(self):
        return{
            "id": self.id,
            "cliente_id": self.cliente_id,
            "endereco_id": self.endereco_id,
            "data": self.data.isoformat() if self.data else None,
            "total": float(self.total),
            "itens": [item.to_dict() for item in self.itens],
        }
