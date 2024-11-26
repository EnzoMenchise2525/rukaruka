$(document).ready(function () {
    // Cargar la primera página de social al cargar la página
    loadSocial(1);

    // Función para cargar social basadas en la página
    function loadSocial(page) {
        $.ajax({
            url: '/ver_social/',  // Update the URL based on your configuration
            data: { page: page },
            type: 'GET',
            success: function (data) {
                $('#noticias-container').html(data.social_html);
                $('#pagination-container').html(data.pagination_html);
            },
            error: function () {
                console.log('Error al cargar social.');
            },
        });
    }

    // Manejar clics en los enlaces de paginación
    $(document).on('click', '.pagination a', function (event) {
        event.preventDefault();
        const page = $(this).attr('href').split('page=')[1];
        loadSocial(page);
    });

    // Cargar social cuando se hace clic en un número de página
    $(document).on('click', '.pagination .page-link', function (event) {
        event.preventDefault();
        const page = $(this).attr('data-page');
        loadSocial(page);
    });
});