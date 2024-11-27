from coffeverse.extensions.database import db

class Cliente(db.Model):
  __tablename__ = 'tb_cliente'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  telefone = db.Column(db.String(15), nullable=False)
  endereco = db.Column(db.String(255), nullable=False)
  senha = db.Column(db.String(255), nullable=False)

  pedidos = db.relationship('Pedido', back_populates='cliente')
  enderecos = db.relationship('EnderecoDeEntrega', back_populates='cliente')

  def to_dict(self):
    return{
      "id": self.id,
      "nome": self.nome,
      "email": self.email,
      "telefone": self.telefone,
      "endereco": self.endereco,
      "senha" : self.senha,
    }