from flask import Flask

app = Flask(__name__)

# Cuando vemos un arroba encima de una funcion es un decorator
@app.route('/')
def home():
    return "Hola mundo flask"

# Estoy ejecutando este script por consola
if __name__ == '__main__':
    app.run(debug=True)