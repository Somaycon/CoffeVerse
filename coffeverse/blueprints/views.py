from flask import Flask, render_template, redirect, jsonify
from coffeverse.extensions.database import db
from coffeverse.models.cliente import Cliente
from coffeverse.models.motoboy import Motoboy

def init_app(app):
  @app.route('/clientes', methods=['GET'])
  def get_all_clients():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])
  
  @app.route('/clientes/<int:id>', methods=['GET'])
  def get_client_by_id(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())

  @app.route('/motoboys', methods=['GET'])
  def get_all_motoboys():
    motoboys = Motoboy.query.all()
    return jsonify([motoboy.to_dict() for motoboy in motoboys])