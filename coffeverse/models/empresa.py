from coffeverse.extensions.database import db

class Empresa(db.Model):
    __tablename__ = 'tb_empresa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    imagem = db.Column(db.LargeBinary) 
    
    produtos = db.relationship('Produto', back_populates='empresa')

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "descricao": self.descricao,
            "imagem": self.imagem,
        }
