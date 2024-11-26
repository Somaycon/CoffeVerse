from flask import Flask, render_template, redirect, jsonify, request
from coffeverse.extensions.database import db
from coffeverse.models.cliente import Cliente
from coffeverse.models.motoboy import Motoboy
from coffeverse.models.pedido import Pedido
from coffeverse.models.itens_pedidos import ItemDoPedido

#cliente

def init_app(app):
  @app.route('/api/clientes', methods=['GET'])
  def get_all_clients():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])
  
  @app.route('/api/clientes/<int:id>', methods=['GET'])
  def get_client_by_id(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())

  @app.route('/api/clientes', methods=['POST'])
  def create_client():
    try:
      response = request.get_json()

      if not response or not all(key in response for key in ["nome", "email", "telefone", "endereco", "senha"]):
        return jsonify({"error": "Dados incompletos"}), 400

      novo_cliente = Cliente (
         nome=response['nome'],
            email=response['email'],
            telefone=response['telefone'],
            endereco=response['endereco'],
            senha=response['senha']
      )

      db.session.add(novo_cliente)
      db.session.commit()

      return jsonify(novo_cliente.to_dict()), 201

    except Exception as e:
      db.session.rollback()
      return jsonify({"Erro": str(e)}), 500

  @app.route('/api/clientes/<int:id>', methods=['PUT'])
  def edit_client(id):
    try:
      cliente = Cliente.query.get(id)
      if not cliente:
        return jsonify({"Erro" : "Cliente não encontrado!"}), 404

      response = request.get_json()

      if "nome" in response:
        cliente.nome = response['nome']
      if "email" in response:
       cliente.email = response['email']
      if "telefone" in response:
        cliente.telefone = response['telefone']
      if "endereco" in response:
        cliente.endereco = response['endereco']
      if "senha" in response:
        cliente.senha = response['senha']

      db.session.commit()

      return jsonify(cliente.to_dict()), 200

    except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 500

  @app.route('/api/clientes/<int:id>', methods=['DELETE'])
  def delete_client(id):
    try:
      cliente = Cliente.query.get(id)

      if not cliente:
        return jsonify({"Erro" : "Cliente não encontrado!"}), 404

      db.session.delete(cliente)
      db.session.commit()

      return jsonify({"message": f"Cliente com ID {id} foi excluído com sucesso!"}), 200

    except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 500

#motoboy

  @app.route('/api/motoboys', methods=['GET'])
  def get_all_motoboys():
    motoboys = Motoboy.query.all()
    return jsonify([motoboy.to_dict() for motoboy in motoboys])
  
  @app.route('/api/motoboys/<int:id>', methods=['GET'])
  def get_motoboy_by_id(id):
    motoboy = Motoboy.query.get_or_404(id)
    return jsonify([motoboy.to_dict()])

  @app.route('/api/motoboys', methods=['POST'])
  def create_motoboy():
    try:
      response = request.get_json()

      if not response or not all(key in response for key in ["nome","telefone",]):
        return jsonify({"Erro": "Dados invalidos!"}), 400

      novo_motoboy = Motoboy(
        nome = response['nome'],
        telefone = response['telefone']
      )

      db.session.add(novo_motoboy)
      db.session.commit()

      return jsonify(novo_motoboy.to_dict()), 201
    
    except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 500

  @app.route('/api/motoboys/<int:id>', methods=['PUT'])
  def edit_motoboy(id):
    try:
      motoboy = Motoboy.query.get(id)

      if not motoboy:
        return jsonify({"Erro" : "Motoboy não encontrado!"}), 404
      
      response = request.get_json()

      if "nome" in response:
          motoboy.nome = response['nome']
      if "telefone" in response:
          motoboy.telefone = response['telefone']
      
      db.session.commit()
      return jsonify(motoboy.to_dict()), 200

    except Exception as e:
      db.session.rollback()
      return jsonify({"Erro": str(e)}), 500
    
  @app.route('/api/motoboys/<int:id>', methods=['DELETE'])
  def delete_motoboy(id):
    try:
      motoboy = Motoboy.query.get(id)

      if not motoboy:
        return jsonify({"Erro" : "Motoboy não encontrado!"}), 404

      db.session.delete(motoboy)
      db.session.commit()
      return jsonify({"message": f"Motoboy com ID {id} foi excluído com sucesso!"}), 200
      
    except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 500
    
#pedidos

  @app.route('/api/pedidos', methods=['GET'])
  def get_all_pedidos():
      pedidos = Pedido.query.all()
      return jsonify([pedido.to_dict() for pedido in pedidos])

  @app.route('/api/pedidos/<int:id>', methods=['GET'])
  def get_pedido_by_id(id):
      pedido = Pedido.query.get_or_404(id)
      return jsonify(pedido.to_dict())

  @app.route('/api/pedidos', methods=['POST'])
  def create_pedido():
      try:
          response = request.get_json()

          if not response or not all(key in response for key in ["cliente_id", "endereco_id", "data", "total"]):
                return jsonify({"error": "Dados incompletos"}), 400

          novo_pedido = Pedido(
              cliente_id=response['cliente_id'],
              endereco_id=response['endereco_id'],
              data=response['data'],
              total=response['total']
          )

          db.session.add(novo_pedido)
          db.session.commit()
          return jsonify(novo_pedido.to_dict()), 201

      except Exception as e:
          db.session.rollback()
          return jsonify({"error": str(e)}), 500

  @app.route('/api/pedidos/<int:id>', methods=['PUT'])
  def edit_pedido(id):
      try:
          pedido = Pedido.query.get(id)
          if not pedido:
              return jsonify({"error": "Pedido não encontrado!"}), 404

          response = request.get_json()

          if "cliente_id" in response:
              pedido.cliente_id = response['cliente_id']
          if "endereco_id" in response:
              pedido.endereco_id = response['endereco_id']
          if "data" in response:
              pedido.data = response['data']
          if "total" in response:
              pedido.total = response['total']

          db.session.commit()
          return jsonify(pedido.to_dict()), 200

      except Exception as e:
          db.session.rollback()
          return jsonify({"error": str(e)}), 500

  @app.route('/api/pedidos/<int:id>', methods=['DELETE'])
  def delete_pedido(id):
      try:
          pedido = Pedido.query.get(id)
          if not pedido:
              return jsonify({"error": "Pedido não encontrado!"}), 404

          db.session.delete(pedido)
          db.session.commit()
          return jsonify({"message": f"Pedido com ID {id} foi excluído com sucesso!"}), 200

      except Exception as e:
          db.session.rollback()
          return jsonify({"error": str(e)}), 500

#Itens do Pedido
    
  @app.route('/api/itens_do_pedido', methods=['GET'])
  def get_all_itens():
      itens = ItemDoPedido.query.all()
      return jsonify([item.to_dict() for item in itens])

  @app.route('/api/itens_do_pedido/<int:id>', methods=['GET'])
  def get_item_by_id(id):
      item = ItemDoPedido.query.get_or_404(id)
      return jsonify(item.to_dict())

  @app.route('/api/itens_do_pedido', methods=['POST'])
  def create_item():
      try:
          response = request.get_json()

          if not response or not all(key in response for key in ["pedido_id", "produto_id", "quantidade", "preco_unitario"]):
              return jsonify({"error": "Dados incompletos"}), 400

          novo_item = ItemDoPedido(
              pedido_id=response['pedido_id'],
              produto_id=response['produto_id'],
              quantidade=response['quantidade'],
              preco_unitario=response['preco_unitario']
          )

          db.session.add(novo_item)
          db.session.commit()
          return jsonify(novo_item.to_dict()), 201

      except Exception as e:
          db.session.rollback()
          return jsonify({"error": str(e)}), 500

  @app.route('/api/itens_do_pedido/<int:id>', methods=['PUT'])
  def edit_item(id):
      try:
          item = ItemDoPedido.query.get(id)
          if not item:
              return jsonify({"error": "Item não encontrado!"}), 404

          response = request.get_json()

          if "pedido_id" in response:
              item.pedido_id = response['pedido_id']
          if "produto_id" in response:
              item.produto_id = response['produto_id']
          if "quantidade" in response:
              item.quantidade = response['quantidade']
          if "preco_unitario" in response:
              item.preco_unitario = response['preco_unitario']

          db.session.commit()
          return jsonify(item.to_dict()), 200

      except Exception as e:
          db.session.rollback()
          return jsonify({"error": str(e)}), 500

  @app.route('/api/itens_do_pedido/<int:id>', methods=['DELETE'])
  def delete_item(id):
      try:
          item = ItemDoPedido.query.get(id)
          if not item:
              return jsonify({"error": "Item não encontrado!"}), 404

          db.session.delete(item)
          db.session.commit()
          return jsonify({"message": f"Item com ID {id} foi excluído com sucesso!"}), 200

      except Exception as e:
          db.session.rollback()
          return jsonify({"error": str(e)}), 500