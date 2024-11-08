from repository.produto_repository import ProdutoRepository
from entity.produto import Produto

class ProdutoService:

    @staticmethod
    def create_produto(produto:object):
        novo_produto = ProdutoRepository.create_produto(produto)
        return novo_produto
        

    @staticmethod
    def atualizar_estoque(id, quantidade):
        produto = ProdutoRepository.get_by_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")
        
        produto.quantidade = quantidade
        return ProdutoRepository.update_produto(produto)

    @staticmethod
    def atualizar_localizacao(id, localizacao):
        produto = ProdutoRepository.get_by_id(id)
        if not produto:
            raise ValueError("Produto não encontrado")
        
        produto.localizacao = localizacao
        return ProdutoRepository.update_produto(produto)

    @staticmethod
    def gerar_relatorio():
        produtos = ProdutoRepository.get_all()
        estoque_baixo = [p.to_dict() for p in produtos if p.quantidade < 10]
        excesso_estoque = [p.to_dict() for p in produtos if p.quantidade > 100]

        return {
            "estoque_baixo": estoque_baixo,
            "excesso_estoque": excesso_estoque,
            "total_produtos": len(produtos)
        }
    
    @staticmethod
    def delete(id:int):
        try:
            return ProdutoRepository.delete_produto(id)
        except Exception as e:
            raise e('Erro ao deletar id')
