from app import db
from entity.produto import Produto
from exception.id_inexistente_exception import IdInexistenteException

class ProdutoRepository:

    @staticmethod
    def get_all():
        '''Função para buscar tudo'''
        return Produto.query.all()

    @staticmethod
    def get_by_id(id:int):
        '''Função para buscar por id'''
        id_produto = Produto.query.get(id)
        if id_produto:
            return id_produto
        raise IdInexistenteException('ID não encontrado no banco de dados')

    @staticmethod
    def create_produto(produto:object):
        '''Função criar produto'''
        try:
            db.session.add(produto)
            db.session.commit()
            return produto
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_produto(produto):
        '''Função atualizar produto'''
        try:
            db.session.commit()
            return produto
        
        except Exception as e:
            db.session.rollback()
            raise e('Erro inesperado ao atualizar dados do produto no banco de dados')

    @staticmethod
    def delete_produto(id:int):
        '''Função deletar produto'''
        try:
            Produto = ProdutoRepository.get_by_id(id)
            if Produto:
                db.session.delete(Produto)
                db.session.commit()
                return True
            raise IdInexistenteException('ID de usuario não encontrado no banco de dados')
        except Exception as e:
            db.session.rollback()
            raise e('Erro inesperado ao excluir produto do banco de dados')
