from flask import Blueprint, jsonify, request
from service.produto_service import ProdutoService
from entity.produto import Produto
from exception.produto_existente_exception import ProdutoExistenteException
from exception.id_inexistente_exception import IdInexistenteException
produto_bp = Blueprint('produtos', __name__)

@produto_bp.route('', methods=['POST'])
def create_produto():
    data = request.get_json()
    produto = Produto(
        nome=data['nome'],
        categoria=data['categoria'],
        quantidade=data['quantidade'],
        preco=data['preco'],
        localizacao=data['localizacao']
    )
    try:
        produto_salvo = ProdutoService.create_produto(produto)
        return jsonify(produto_salvo.to_dict()), 201
    except ProdutoExistenteException as pee:
        return jsonify({'Error': str(pee)}), 400
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@produto_bp.route('/<int:produto_id>/estoque', methods=['PUT'])
def atualizar_estoque(produto_id):
    data = request.get_json()
    try:
        produto = ProdutoService.atualizar_estoque(produto_id, data.get('quantidade'))
        return jsonify(produto.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@produto_bp.route('/<int:produto_id>/localizacao', methods=['PUT'])
def atualizar_localizacao(produto_id):
    data = request.get_json()
    try:
        produto = ProdutoService.atualizar_localizacao(produto_id, data.get('localizacao'))
        return jsonify(produto.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@produto_bp.route('/relatorio', methods=['GET'])
def gerar_relatorio():
    relatorio = ProdutoService.gerar_relatorio()
    return jsonify(relatorio), 200

@produto_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        produto = ProdutoService.delete(id)
        return jsonify({"Delete":produto}), 200
    except IdInexistenteException as e:
        return jsonify({"Error": str(e)}), 404
    except Exception as e:
        return jsonify({"Error": "Erro Inesperado, tente novamente mais tarde"}), 500
