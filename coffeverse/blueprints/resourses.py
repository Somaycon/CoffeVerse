from flask import Flask, render_template, redirect, jsonify, request
from coffeverse.extensions.database import db
from coffeverse.models.cliente import Cliente
from coffeverse.models.motoboy import Motoboy

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