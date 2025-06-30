console.clear();
const form = document.getElementById("movies");
fetch('/api/movie_titles/')
    .then(res => res.json())
    .then(data => {
        addtolist(data.titles);
    });

function addtolist(headers) {
    for (let i = 0; i < headers.length; i++) {
        const opt = document.createElement("option");
        opt.value = headers[i];
        opt.textContent = headers[i];
        form.appendChild(opt);
    }
}


