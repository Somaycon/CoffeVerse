from coffeverse.extensions.database import db

class EnderecoEntrega(db.Model):
    __tablename__ = 'tb_enderecos_entrega'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('tb_cliente.id'), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    cep = db.Column(db.String(20), nullable=False)

    cliente = db.relationship('Cliente', back_populates='enderecos')
    pedidos = db.relationship('Pedido', back_populates='endereco')

    def to_dict(self):
        return {
            "id": self.id,
            "rua": self.rua,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "cep": self.cep,
        }
