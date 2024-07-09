let submitButton = document.querySelector("#Formulario #Crear");

submitButton.addEventListener("click", () =>{
    let data_post = {
        'nombre': document.querySelector("#Formulario #Titulo").value,
        'descripcion': document.querySelector("#Formulario #Descripcion").value
    }

    fetchData(
        "http://127.0.0.1:5000/api/tasks/create/",
        "POST",
        (data) => {
            // quiero resetar el formulario para no duplicar la informacion
            document.querySelector("#Formulario").reset();
            // cambiar la ruta, enviarla a tareas pendientes
            window.location.replace("../index.html#TareasPendientes");
        },
        data_post
    );
});



