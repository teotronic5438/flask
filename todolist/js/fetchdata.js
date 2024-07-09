// como hablo con el backend, con el fetch
function fetchData(url, method, callback, data = null) {
    // Configuración de las opciones de la solicitud
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',  // Especifica que el contenido es JSON
        },
        body: data ? JSON.stringify(data) : null,  // Convierte los datos a JSON si hay datos
    };

    // Realiza la solicitud HTTP
    fetch(url, options)
        .then(response => response.json())  // Convierte la respuesta a JSON
        .then(data => {
            callback(data);  // Llama a la función de callback con los datos recibidos
        })
        .catch(error => console.log("Ocurrio un error!: " + error));  // Manejo de errores
}