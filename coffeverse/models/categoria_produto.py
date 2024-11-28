from coffeverse.extensions.database import db

class CategoriaProduto(db.Model):
    __tablename__ = 'tb_categoria_produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(30), nullable=False, unique=True)
    
    # Validação do comprimento do nome usando o SQLAlchemy CheckConstraint
    __table_args__ = (
        db.CheckConstraint('LENGTH(nome) > 0', name='CHK_nome_categoria'),
    )
    
    # Relacionamento com a tabela Produto
    produtos = db.relationship('Produto', back_populates='categoria')

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }
