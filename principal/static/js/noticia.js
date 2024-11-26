$(document).ready(function () {
    // Cargar la primera página de noticias al cargar la página
    loadNews(1);

    // Función para cargar noticias basadas en la página
    function loadNews(page) {
        $.ajax({
            url: '/ultimas_noticias/',  // Ajusta la URL según tu configuración
            data: { page: page },
            type: 'GET',
            success: function (data) {
                $('#noticias-container').html(data.noticias_html);
                $('#pagination-container').html(data.pagination_html);
            },
            error: function () {
                console.log('Error al cargar noticias.');
            },
        });
    }

    // Manejar clics en los enlaces de paginación
    $(document).on('click', '.pagination a', function (event) {
        event.preventDefault();
        const page = $(this).attr('href').split('page=')[1];
        loadNews(page);
    });

    // Cargar noticias cuando se hace clic en un número de página
    $(document).on('click', '.pagination .page-link', function (event) {
        event.preventDefault();
        const page = $(this).attr('data-page');
        loadNews(page);
    });
});