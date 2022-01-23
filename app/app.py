from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)

    from views import products
    app.register_blueprint(products.bp, url_prefix="/products")

    add_swagger_docs(app)

    return app


def add_swagger_docs(app):
    SWAGGER_URL = '/docs/'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Blabla API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
