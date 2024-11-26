function mostrarVistaPrevia() {
    // Obtener los valores de los campos del formulario
    var titulo = document.getElementById("titulo_reconstruccion").value;
    var fecha = document.getElementById("fecha_reconstruccion").value;
    var texto = document.getElementById("texto_reconstruccion").value;
    var imagen = document.getElementById("imagen_reconstruccion").files[0];
    var servicio = document.getElementById("Servicio").value;
    var ciudad = document.getElementById("nombre_ciudad").value;
    var tipoServicio = document.getElementById("nombre_tipo_servicio").value;

    // Verificar si se ha seleccionado una imagen
    if (!imagen) {
        alert("Por favor, seleccione una imagen antes de crear la noticia.");
        return; // Detener la función si no hay imagen
    }

    // Crear un elemento de imagen
    var img = document.createElement("img");
    img.src = URL.createObjectURL(imagen);
    img.style.maxWidth = "100%";

    // Crear un elemento para mostrar la información de la noticia
    var infoNoticia = document.createElement("div");
    infoNoticia.className = "noticia texto-negro"; // Agregar la clase "texto-negro"

    // Obtener los componentes de la fecha
    var fechaDate = new Date(fecha);
    var dia = fechaDate.getDate();
    var mes = fechaDate.toLocaleString('default', { month: 'long' }); // Obtener el nombre del mes
    var año = fechaDate.getFullYear();

    // Agregar contenido a infoNoticia
    infoNoticia.innerHTML += `
        <h2>${titulo}</h2>
        <p>Fecha: ${dia} de ${mes} de ${año}</p> <!-- Mostrar la fecha en el formato deseado -->
        <p>Tipo de Servicio: ${servicio}</p>
        <p>${ciudad}</p>
        <p>${tipoServicio}</p>
        <p>${texto}</p>
    `;

    // Reemplazar el contenido anterior con la nueva noticia
    var contenedorNoticia = document.getElementById("contenedor-de-noticia");
    contenedorNoticia.innerHTML = ''; // Limpiar el contenedor anterior
    contenedorNoticia.appendChild(img);
    contenedorNoticia.appendChild(infoNoticia);
    
    
}

// -----------------------------------------------------------------------------//
// -------------------------- cargar-Imagenes -----------------------------//


function cargarImagenes() {
    var contenedorImagenes = document.getElementById("contenedor-imagenes");

    // Limpiar el contenido anterior en el contenedor
    contenedorImagenes.innerHTML = '';

    // Obtener todas las entradas de imágenes (imagen1, imagen2, ...)
    var inputsImagen = document.querySelectorAll('input[type="file"][id^="imagen"]');

    for (var i = 0; i < inputsImagen.length; i++) {
        var input = inputsImagen[i];

        for (var j = 0; j < input.files.length; j++) {
            var imagen = document.createElement("img");
            imagen.src = URL.createObjectURL(input.files[j]);
            imagen.className = "imagen-cargada";

            // Agregar un ícono de "X" en un círculo rojo
            var iconoEliminar = document.createElement("i");
            iconoEliminar.className = "fas fa-times-circle icono-eliminar";
            iconoEliminar.onclick = function (event) {
                // Acceder al contenedor padre y eliminarlo
                var contenedor = event.target.parentNode;
                contenedorImagenes.removeChild(contenedor);

                // También puedes eliminar el archivo del input file si es necesario
                input.value = null;
            };

            // Crear un contenedor para la imagen y el ícono de eliminación
            var contenedor = document.createElement("div");
            contenedor.className = "imagen-container";
            contenedor.id = "imagen-container-" + i + "-" + j; // Identificador único
            contenedor.appendChild(imagen);
            contenedor.appendChild(iconoEliminar);

            contenedorImagenes.appendChild(contenedor);
        }
    }
}



// -----------------------------------------------------------------------------//
// -------------------------- Publicar Noticia -----------------------------//
// -----------------------------------------------------------------------------//

function publicarNoticia() {
    // Llama a la función mostrarVistaPrevia para crear el contenedor con los datos ingresados
    mostrarVistaPrevia();

    // Muestra un cuadro de diálogo de confirmación
    var confirmacion = confirm("¿Desea agregar la noticia?");

    // Verifica la respuesta del usuario
    if (confirmacion) {
        // Obtén los datos necesarios para la solicitud AJAX
        var titulo = document.getElementById("titulo_reconstruccion").value;
        var fecha = document.getElementById("fecha_reconstruccion").value;
        var texto = document.getElementById("texto_reconstruccion").value;
        var servicio = document.getElementById("Servicio").value;
        var ciudad = document.getElementById("texto_ciudad").value;
        var tipoServicio = document.getElementById("texto_tipo_servicio").value;

        // Crea un objeto FormData para enviar datos y archivos
        var formData = new FormData();
        formData.append('titulo', titulo);
        formData.append('fecha', fecha);
        formData.append('texto', texto);
        formData.append('servicio', servicio);
        formData.append('ciudad', ciudad);
        formData.append('tipoServicio', tipoServicio);

        // Agrega la imagen seleccionada al FormData
        var imagen = document.getElementById("imagen_reconstruccion").files[0];
        formData.append('imagen', imagen);

        // Realiza una solicitud AJAX para guardar la noticia en el servidor
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/admin_agregar_reconstruccion/', true); // Reemplaza '/admin_agregar_noticia/' por la URL correcta
        xhr.onload = function () {
            if (xhr.status === 200) {
                alert("Noticia publicada con éxito.");
                // Limpia el contenedor de imágenes después de publicar
                var contenedorImagenes = document.getElementById("contenedor-imagenes");
                contenedorImagenes.innerHTML = '';
                // También puedes reiniciar otros campos del formulario si es necesario
                document.getElementById("titulo_reconstruccion").value = '';
                document.getElementById("fecha_reconstruccion").value = '';
                document.getElementById("texto_reconstruccion").value = '';
                document.getElementById("imagen_reconstruccion").value = '';
                document.getElementById("Servicio").value = '';
                document.getElementById("texto_ciudad").value = '';
                document.getElementById("texto_tipo_servicio").value = '';
                // Redirige a la página de admin_agregar_intSocial.html para agregar una nueva noticia
                window.location.href = "/admin_agregar_reconstruccion/";
            } else {
                alert("Hubo un error al guardar la noticia.");
            }
        };
        xhr.send(formData);
    } else {
        alert("La noticia no se ha agregado.");
    }
}