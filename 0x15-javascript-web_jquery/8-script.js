$(document).ready(function () {
  const $ul = $('#list_movies');

  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (response) {
      response.results.forEach(function (movie) {
        $ul.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
