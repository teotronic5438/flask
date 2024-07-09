// Contenedor donde se dibujan las tareas
let taskContainer = document.querySelector('.tareas-container');


// Template de tarea Pendiente
let taskPendingTemplateReference = document.querySelector('.tarea.pendiente.template');

// Template de tarea Completada
let taskCompletedTemplateReference = document.querySelector('.tarea.completada.template');

// Template de tarea Archivada
let taskArchivedTemplateReference = document.querySelector('.tarea.archivada.template');

// Hago una copia de las referencias
let pendingTask = taskPendingTemplateReference.cloneNode(true);
let completedTask = taskCompletedTemplateReference.cloneNode(true);
let archivedTask = taskArchivedTemplateReference.cloneNode(true);

// Quito del documento los templates
taskPendingTemplateReference.remove();
taskCompletedTemplateReference.remove();
taskArchivedTemplateReference.remove();

fetchData("http://127.0.0.1:5000/api/tasks/pending/",
        "GET", 
        (data) => {
        console.log(data);
        
        let tareas = [];

        // recorro la lista de dtaeras obtenidas
        for (const tarea of data){
            console.log(tarea);

            // paso 1: duplicar la plantilla de tarea pendietna
            let newTask = pendingTask.cloneNode(true);

            // paso 2: Completar la tarea con los datos reales
            newTask.querySelector("h3 .titulo").innerHTML = tarea.nombre;
            newTask.querySelector(".descripcion").innerHTML = tarea.descripcion;
            newTask.querySelector(".fecha").innerHTML = tarea.fecha_creacion;
            newTask.querySelector(".task_id").value = tarea.id;

            // agrego la nueva tarea al listado de tareas para ver en el viewport
            tareas.push(newTask)

            // paso 3: Agregarla al frontend

        }

        // Accion doble
        // ReplaceChildren borra todo el contenido interno y agrega lo que yo le diga
        taskContainer.replaceChildren(...tareas);
});

















// fetch("http://127.0.0.1:5000/api/tasks/pending/", {
//     method: "GET"
// })
// .then(response => {
//     if (!response.ok) {
//         throw new Error('Network response was not ok ' + response.statusText);
//     }
//     return response.json();
// })
// .then(data => {
//     console.log(data);
// })
// .catch(error => {
//     console.error('There was a problem with the fetch operation:', error);
// });