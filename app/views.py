from flask import jsonify, request   # para generar json
# para poder crear una tarea tengo que exportarme "request" de flask
# consultar los datos que me llegan del usuario

def index():
    return jsonify({
        'mensaje': 'Hola api Todo List'
    })

def get_pending_tasks():
    tasks = [
        {
            'id': 1,
            'nombre': 'Tarea 1 Pendiente',
            'descripcion': 'Tarea 1 Description',
            'completada': False,
            'activo': True,
            'fecha_creacion': '2024-01-01'    
        },
        {
            'id': 2,
            'nombre': 'Tarea 2 Pendiente',
            'descripcion': 'Tarea 2 Description',
            'completada': False,
            'activo': True,
            'fecha_creacion': '2024-01-01'
        }
    ]
    return jsonify(tasks)

def get_completed_tasks():
    tasks = [
        {
            'id': 1,
            'nombre': 'Tarea 1 Completada',
            'descripcion': 'Tarea 1 Descripcion',
            'completada': False,
            'activo': True,
            'fecha_creacion': '2024-01-01'
        },{
            'id': 2,
            'nombre': 'Tarea 2 Completada',
            'descripcion': 'Tarea 2 Descripcion',
            'completada': False,
            'activo': True,
            'fecha_creacion': '2024-01-01'
        }
    ]
    return jsonify(tasks)

def get_archived_tasks():
    tasks = [
        {
            'id': 1,
            'nombre': 'Tarea 1 Archivada',
            'descripcion': 'Tarea 1 Descripcion',
            'completada': False,
            'activo': True,
            'fecha_creacion': '2024-01-01'
        },{
            'id': 2,
            'nombre': 'Tarea 2 Archivada',
            'descripcion': 'Tarea 2 Descripcion',
            'completada': False,
            'activo': True,
            'fecha_creacion': '2024-01-01'
        }
    ]
    return jsonify(tasks)

# tambien creo uno para busquedas unitarias o tareas individuales
# consulto si existe y en ese caso la devuelvo
def get_task(task_id):
    task = {
        'id': task_id
    }
    return jsonify(task)

# para leer la informacion que el usuario manda por peticion Y CREAR TAREAS
def create_task():
    #datos recibidos en formato json
    data = request.json
    return jsonify({'mensaje': 'task created successfully', 'data': data}), 201

# TAMBIEN PUEDO ACTUALIZAR LAS TAREAS POR ID
def update_task(task_id):
    # datos recibidos en formato json
    data = request.json
    return jsonify({'mensaje': 'task updated successfully', 'data': data, 'id': task_id})


# Ahora preparamos las tres vistas: Archivar una tarea, completar / marcar como pendiente
# Pasa parametro activo a inactivo
def archive_task(task_id):
    return jsonify({'mensaje': 'task archived successfully', 'id':task_id})

# Para los set y reset para parametro completada de activo a inactivo
def set_complete_tasks(task_id):
    return jsonify({'message': 'task updated successfully', 'id': task_id})

def reset_complete_task(task_id):
    return jsonify({'message': 'task updated successfully', 'id': task_id})