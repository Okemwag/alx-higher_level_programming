// JavaScript script that fetches and lists the title for all movies by using given URL.
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const film of data.results) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
