function mostrarImagenDePerfil(event) {
    const input = event.target;
    const reader = new FileReader();
    reader.onload = function () {
        const dataURL = reader.result;
        const imagenDePerfil = document.getElementById('imagenDePerfil');
        imagenDePerfil.src = dataURL;
    };
    reader.readAsDataURL(input.files[0]);
}

const contenedorImagen = document.getElementById('contenedor_imagen');
        const inputImagenFondo = document.getElementById('imagen_de_fondo_input');

        inputImagenFondo.addEventListener('change', (event) => {
            const archivo = event.target.files[0];
            if (archivo) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    contenedorImagen.style.backgroundImage = `url('${e.target.result}')`;
                    contenedorImagen.style.backgroundSize = 'cover';
                    contenedorImagen.style.backgroundPosition = 'center';
                    contenedorImagen.style.backgroundRepeat = 'no-repeat';
                };
                reader.readAsDataURL(archivo);
            }
        });