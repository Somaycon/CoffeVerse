from coffeverse.extensions.database import db

class EnderecoDeEntrega(db.Model):
    __tablename__ = 'tb_enderecos_de_entrega'
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('tb_cliente.id'), nullable=False)
    
    cliente = db.relationship('Cliente', back_populates='enderecos')
    pedidos = db.relationship('Pedido', back_populates='endereco')
    
    def to_dict(self):
        return {
            "id": self.id,
            "rua": self.rua,
            "numero": self.numero,
            "cidade": self.cidade,
            "estado": self.estado,
        }
