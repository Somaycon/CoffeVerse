from flask import Flask
from coffeverse.extensions import config

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    config.load_extentions(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
