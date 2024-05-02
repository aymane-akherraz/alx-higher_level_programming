$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(e => {
      $('#list_movies').append($('<li></li>').text(e.title));
    });
  });
});
