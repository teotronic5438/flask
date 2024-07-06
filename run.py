from flask import Flask
from app.views import * # me traigo todo
from app.database import test_connection

app = Flask(__name__)

# Rutas de la API-REST
app.route('/', methods=['GET'])(index)  # en lugar de decorator uso una funcion que me provee flask (a barra devuelve index de view)

# Conexion a BBDD
test_connection()

if __name__ == '__main__':
    app.run(debug=True)