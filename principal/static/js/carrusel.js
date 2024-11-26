// -----------------------------------------------------------------------------//
// -------------------------- Carrusel -----------------------------------------//
// -----------------------------------------------------------------------------//

var carruselIndex = 0;
mostrarCarrusel();

function mostrarCarrusel() {
    var i;
    var imagenesCarrusel = document.getElementsByClassName("carrusel-elemento");
    
    for (i = 0; i < imagenesCarrusel.length; i++) {
        imagenesCarrusel[i].style.display = "none";
    }
    
    carruselIndex++;
    
    if (carruselIndex > imagenesCarrusel.length) {
        carruselIndex = 1;
    }
    
    imagenesCarrusel[carruselIndex - 1].style.display = "block";
    setTimeout(mostrarCarrusel, 3000);
}

// Variables para el seguimiento del scroll
let prevScrollPos = window.pageYOffset;
const header = document.querySelector('header');

// Detectar el desplazamiento de la página
window.addEventListener('scroll', function() {
    const currentScrollPos = window.pageYOffset;
    if (prevScrollPos > currentScrollPos) {
        // El usuario está haciendo scroll hacia arriba, muestra el menú
        header.style.top = '0';
    } else {
        // El usuario está haciendo scroll hacia abajo, oculta el menú
        header.style.top = '-100px';
    }
    prevScrollPos = currentScrollPos;
});
