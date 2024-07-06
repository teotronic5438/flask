from flask import Flask
from app.views import * # me traigo todo
from app.database import test_connection, init_app

app = Flask(__name__)

'''
La sentencia app = Flask(__name__) en una aplicación Flask realiza lo siguiente:

Crea una instancia de la aplicación Flask:

Flask es una clase en el framework Flask, y app es una instancia de esa clase.
Esta instancia de Flask representa la aplicación web en sí misma.
Configura el nombre del módulo o paquete de la aplicación:

El argumento __name__ es una variable especial en Python que representa el nombre del módulo actual.
Al pasar __name__ al constructor Flask, Flask puede determinar la ubicación del módulo y utilizarla para encontrar recursos
 como archivos estáticos y plantillas.
También permite a Flask conocer el contexto en el cual se está ejecutando la aplicación, lo cual es útil para varias 
 operaciones internas del framework.
En resumen, app = Flask(__name__) inicializa la aplicación Flask y configura el entorno en el cual se ejecutará, 
 utilizando el nombre del módulo actual para poder localizar recursos y gestionar la configuración de manera adecuada.
'''

# Rutas de la API-REST
app.route('/', methods=['GET'])(index)  
# Se define la ruta para la raíz ('/') y se asigna la función index de views

'''
Comandos para entorno virtual:
    ./activate                  - Activa el entorno virtual
    deactivate                  - Desactiva el entorno virtual
    pip freeze > requirements.txt - Crea un archivo txt con las dependencias usadas
    pip install -r requirements.txt - Instala las dependencias desde el archivo txt
'''

# Conexion a BBDD
try:
    # test_connection()
    init_app(app)
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

if __name__ == '__main__':
    app.run(debug=True)