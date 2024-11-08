from app import db

class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    localizacao = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "localizacao": self.localizacao
        }
