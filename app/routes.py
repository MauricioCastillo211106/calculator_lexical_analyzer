from flask import Blueprint, request, jsonify
from lexer.lexer import lex

bp = Blueprint('calc', __name__, url_prefix='/calculate')

@bp.route('/', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression', '')

    try:
        tokens = list(lex(expression))
        # En una implementación completa, aquí se construiría y evaluaría el árbol de derivación.
        return jsonify({'tokens': tokens}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
