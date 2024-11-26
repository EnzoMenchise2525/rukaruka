$(document).ready(function () {
    // Toggle the mobile menu when clicking the hamburger icon
    $(".mobile-menu-icon").click(function () {
        $("nav ul.menu").toggleClass("mobile-expanded");
    });

    // Mostrar el submenu al pasar el cursor sobre "Proyectos" en dispositivos móviles
    $("nav ul.menu .submenu > a").on("mouseenter", function (e) {
        e.preventDefault();

        const submenu = $(this).next(".submenu-items");

        // Mostrar el submenu al pasar el cursor sobre "Proyectos"
        submenu.slideDown(200);
        $(this).parent('.submenu').addClass('active');
    });

    // Ocultar el submenu al quitar el cursor de "Proyectos" en dispositivos móviles
    $("nav ul.menu .submenu").on("mouseleave", function () {
        const submenu = $(this).find(".submenu-items");

        // Ocultar el submenu al quitar el cursor de "Proyectos"
        submenu.slideUp(200);
        $(this).removeClass('active');
    });

    // Cerrar submenús al hacer clic fuera del menú en dispositivos móviles
    $(document).on("click", function (e) {
        if ($("nav ul.menu").hasClass("mobile-expanded")) {
            if (!$(e.target).closest("nav ul.menu").length) {
                $("nav ul.menu .submenu-items").slideUp(200);
                $("nav ul.menu .submenu.active").removeClass('active');
            }
        }
    });

    // Ocultar las opciones de "Viviendas" y "Barrios" por defecto en dispositivos móviles
    $("nav ul.menu .submenu .submenu-items").hide();
});

