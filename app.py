from flask import Flask
from config import Config
from db import db
import init_db
from controller.produto_controller import produto_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

init_db.init_db(app)

app.register_blueprint(produto_bp, url_prefix='/GE')


if __name__ == "__main__":
    app.run(debug=True)