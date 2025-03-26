let file = '/static/movie_dataset.csv'

console.clear();
const form = document.getElementById("movies");
fetch(file)
    .then(Response => Response.text())
    .then(csvText => {
        const rows = csvText.split('\n');
        console.log(rows)
        const names = rows
            .map(trimarr)
            .filter((title) => title);
        addtolist(names)
    })


function addtolist(headers) {
    for (let i = 1; i < headers.length; i++) {
        opt = document.createElement("option");
        opt.value = headers[i];
        opt.textContent = headers[i];
        form.appendChild(opt);
        
    }
}

function trimarr(filmdata) {
    const film = filmdata.split(",");
    if (film.length > 1) {
        return film[7].trim();
    }
    return null
}




