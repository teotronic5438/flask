from flask import Flask
from app.views import * # me traigo todo
from app.database import * # me traigo todo

app = Flask(__name__)

# Se define la ruta para la raíz ('/') y se asigna la función index de views
# Rutas de la API-REST
app.route('/', methods=['GET'])(index)

# CRUD
app.route('/api/tasks/pending/', methods=['GET'])(get_pending_tasks)
app.route('/api/tasks/completed/', methods=['GET'])(get_completed_tasks)
app.route('/api/tasks/archived/', methods=['GET'])(get_archived_tasks)

# hace una peticion para una tarea particular pasando como parametro en URL un entero que sera leido como "task_id"
app.route('/api/tasks/fetch/<int:task_id>', methods=['GET'])(get_task)

# tambien para cuando creo las tareas o las modifico
app.route('/api/tasks/create/', methods=['POST'])(create_task)
app.route('/api/tasks/update/<int:task_id>', methods=['PUT'])(update_task)

# ahora preparo as rutas para cuando completo, archivo o reseteo una tarea
# verificar la declaracion de intencion para ver que accion voy a ejecutar y programar la misma
app.route('/api/tasks/archive/<int:task_id>', methods=['DELETE'])(archive_task)
app.route('/api/tasks/complete/set/<int:task_id>', methods=['PUT'])(set_complete_tasks)
app.route('/api/tasks/complete/reset/<int:task_id>', methods=['PUT'])(reset_complete_task)

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
    create_table_tareas()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

if __name__ == '__main__':
    app.run(debug=True)