from coffeverse.extensions.database import db

class Motoboy(db.Model):
  __tablename__ = 'tb_motoboy'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  telefone = db.Column(db.String(15), nullable=False)

  def to_dict(self):
    return {
      "id" : self.id,
      "nome" : self.nome,
      "telefone" : self.telefone,
    }