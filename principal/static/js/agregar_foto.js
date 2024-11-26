document.getElementById('seleccionar_foto').addEventListener('click', function() {
    document.getElementById('perfil_foto_input').click();
});

document.getElementById('perfil_foto_input').addEventListener('change', function() {
    var input = this;
    var file = input.files[0];
    var img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.onload = function() {
        // Muestra la imagen previsualizada
        document.body.appendChild(img);
        // Oculta el botón "Seleccionar Foto" y muestra el botón "Subir Foto"
        document.getElementById('seleccionar_foto').style.display = 'none';
        document.getElementById('subir_foto').style.display = 'block';
    };

    document.getElementById('subir_foto').addEventListener('click', function() {
        // Sube la foto al servidor aquí
        // Puedes utilizar AJAX o enviar el formulario para guardar la foto
        // Asegúrate de configurar tu vista para manejar la carga de la foto
        // y almacenarla en la base de datos
        // Después de subir la foto, puedes redirigir al usuario o actualizar la página según tus necesidades
    });
});