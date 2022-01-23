from flask import jsonify
from flask import Blueprint

bp = Blueprint('products', __name__)


@bp.route('/', methods=['GET'])
def get_products():
    return jsonify({}), 200
