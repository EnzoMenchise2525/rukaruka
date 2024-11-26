function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.querySelector("table");
    switching = true;
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];
            y = rows[i + 1].getElementsByTagName("td")[n];

            // Parsear las fechas antes de comparar
            var xDate = parseDate(x.innerHTML);
            var yDate = parseDate(y.innerHTML);

            if (dir == "asc") {
                if (xDate > yDate) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (xDate < yDate) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }

    // Actualizar la flecha
    updateArrow(dir);
}

// Función para parsear fechas en formato "d/m/Y"
function parseDate(dateString) {
    var parts = dateString.split("/");
    return new Date(parts[2], parts[1] - 1, parts[0]);
}

// Función para actualizar la flecha según la dirección de ordenación
function updateArrow(direction) {
    var arrow = document.getElementById("arrow");
    arrow.innerHTML = direction === "asc" ? "&#x25B2;" : "&#x25BC;";
}



// Función para parsear fechas en formato "d/m/Y"
function parseDate(dateString) {
    var parts = dateString.split("/");
    return new Date(parts[2], parts[1] - 1, parts[0]);
}

function confirmDelete() {
    return confirm('¿Está seguro de borrar la noticia?');
}






// #################################################################################################################################