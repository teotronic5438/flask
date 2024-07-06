from flask import Flask

app = Flask(__name__)

# Cuando vemos un arroba encima de una funcion es un decorator
@app.route('/')
def home():
    return "Hola mundo flask"
'''
    ./activate = activa entorno virtual
    deactivate = desactiva entorno virtual
'''

# Estoy ejecutando este script por consola
# en criollo, este if significa qe estoy ejecutando este script por consola
# es decir: python hello.py
if __name__ == '__main__':
    app.run(debug=True)