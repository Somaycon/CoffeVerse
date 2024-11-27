from flask import Flask, render_template, redirect

def init_app(app):
  @app.route('/')
  def index():
    return render_template('base.html')