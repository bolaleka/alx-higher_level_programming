$(document).ready(function() {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(url, function(data) {
    const movies = data.results;
    const list = $('UL#list_movies');
    movies.forEach(function(movie) {
      list.append($('<li>').text(movie.title));
    });
  });
});
