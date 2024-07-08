import os
import psycopg2
from flask import g
from dotenv import load_dotenv  
#cargo lo que preciso de .env (se installo un paquete para manejarlo mejor python-dotenv==1.0.1)

# Cargar variable de entorno desde el archivo .env
load_dotenv()

# Configuracion de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user' : os.getenv('DB_USERNAME'),
    'password' : os.getenv('DB_PASSWORD'),
    'host' : os.getenv('DB_HOST'),
    'database' : os.getenv('DB_NAME'),
    'port' : os.getenv('DB_PORT', 5432)
}

# Funcion para obtenerla conexion a la base de datos
def get_db():
    if 'db' not in g:
        try:
            g.db = psycopg2.connect(**DATABASE_CONFIG)
        except psycopg2.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise
    return g.db

# Funcion para cerrar la conexion a la base de datos
def close_db(e=None):
    # Extraer la conexion a la base de datos de 'g' y eliminarla
    db = g.pop('db', None)

    # Su la conexion existe, cerrarla
    if db is not None:
        db.close()

# Funcion para inicializar la aplicacion con el manejo de la base de datos
def init_app(app):
    app.teardown_appcontext(close_db)


# tengo los datos basicos para la conexion a la bbdd
# los datos de la bbdd los leo del .env
def test_connection():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        # creo un cursor para hablar con la bbdd
        cur = conn.cursor()

        # commit guarda los cambios en postgres
        conn.commit()

        cur.close() # cierro cursor
        conn.close() # cierro conexion a la bbdd
        print("Conexión exitosa a la base de datos")
    except psycopg2.DatabaseError as e:
        print(f"Error al conectar a la base de datos: {e}")

def create_table_tareas():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas(
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            descripcion VARCHAR(300) NOT NULL,
            fecha_creacion DATE NOT NULL,
            completada BOOLEAN NOT NULL,
            activa BOOLEAN NOT NULL
        );
        """)
    conn.commit()

    cur.close()
    conn.close()