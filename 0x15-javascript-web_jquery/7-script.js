$(document).ready(function () {
  const $div = $('#character');

  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (response) {
      $div.text(response.name);
    }
  });
});
