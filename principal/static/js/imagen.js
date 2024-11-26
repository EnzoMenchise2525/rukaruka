function mostrarImagenAmpliada(url) {
    // Crear un elemento de imagen para mostrar la imagen ampliada
    var imagenAmpliada = document.createElement("img");
    imagenAmpliada.src = url;
    imagenAmpliada.style.width = "70%"; // Ajustar el ancho de la imagen al 70% del contenedor
    imagenAmpliada.style.height = "auto"; // Ajustar la altura automáticamente según la proporción

    // Crear un contenedor para el modal
    var modal = document.createElement("div");
    modal.style.position = "fixed";
    modal.style.zIndex = "1";
    modal.style.left = "0";
    modal.style.top = "0";
    modal.style.width = "100%";
    modal.style.height = "100%";
    modal.style.overflow = "auto";
    modal.style.backgroundColor = "rgba(0,0,0,0.9)";
    modal.style.display = "flex";
    modal.style.alignItems = "center";
    modal.style.justifyContent = "center";

    // Agregar la imagen ampliada al modal
    modal.appendChild(imagenAmpliada);

    // Añadir el modal al cuerpo del documento
    document.body.appendChild(modal);

    // Permitir que el usuario cierre el modal haciendo clic fuera de la imagen
    modal.onclick = function() {
        modal.style.display = "none";
    };
}
