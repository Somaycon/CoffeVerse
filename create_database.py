from coffeverse.extensions.database import db
from coffeverse import create_app
from coffeverse.models import cliente

app = create_app()
with app.app_context():
    db.create_all()