from flask import jsonify   # para generar json

def index():
    return jsonify({
        'mensaje': 'Hola apit Todo List'
    })