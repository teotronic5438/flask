from flask import jsonify, request   # para generar json
# para poder crear una tarea tengo que exportarme "request" de flask
# consultar los datos que me llegan del usuario
from app.models import *
from datetime  import date

def index():
    return jsonify({
        'mensaje': 'Hola api Todo List'
    })

def get_pending_tasks():
    tasks = Task.get_all_pending()
    return jsonify([task.serialize() for task in tasks])

def get_completed_tasks():
    tasks = Task.get_all_completed()
    return jsonify([task.serialize() for task in tasks])
    # return jsonify([task.serialize() for task in tasks])

def get_archived_tasks():
    tasks = Task.get_all_archived()
    return jsonify([task.serialize() for task in tasks])


# tambien creo uno para busquedas unitarias o tareas individuales
# consulto si existe y en ese caso la devuelvo
def get_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(task.serialize())


# para leer la informacion que el usuario manda por peticion Y CREAR TAREAS
def create_task():
    data = request.json
    new_task = Task(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        fecha_creacion=date.today().strftime('%Y-%m-%d'),
        completada=False,
        activa=True
    )
    new_task.save()
    return jsonify({'message': 'Task created successfully'}), 201

# TAMBIEN PUEDO ACTUALIZAR LAS TAREAS POR ID
def update_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    data = request.json
    task.nombre = data['nombre']
    task.descripcion = data['descripcion']
    task.save()
    return jsonify({'message': 'Task updated successfully'})


# Ahora preparamos las tres vistas: Archivar una tarea, completar / marcar como pendiente
# Pasa parametro activo a inactivo
def archive_task(task_id):
    return jsonify({'mensaje': 'task archived successfully', 'id':task_id})

# Para los set y reset para parametro completada de activo a inactivo
def __complete_tasks(task_id, status):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    
    task.completada = status
    task.activated = True
    task.save()
    return jsonify({'mensaje': 'Task updated successfully'})

def set_complete_tasks(task_id):
    return __complete_tasks(task_id, True)

def reset_complete_task(task_id):
    return __complete_tasks(task_id, False)