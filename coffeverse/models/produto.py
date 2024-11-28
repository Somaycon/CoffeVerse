from coffeverse.extensions.database import db

class Produto(db.Model):
    __tablename__ = 'tb_produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(255))
    preco = db.Column(db.Numeric(5, 2))
    empresa_id = db.Column(db.Integer, db.ForeignKey('tb_empresa.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('tb_categoria_produto.id'), nullable=False)
    imagem = db.Column(db.LargeBinary)
    status = db.Column(db.Enum('Disponível', 'Indisponível', name='status_enum'), nullable=False)

    produtos = db.relationship('ItensDoPedido', back_populates='produto')

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": float(self.preco) if self.preco else None,
            "empresa_id": self.empresa_id,
            "categoria_id": self.categoria_id,
            "imagem": self.imagem,
            "status": self.status,
        }
