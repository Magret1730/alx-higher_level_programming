$(document).ready(function () {
  const $div = $('#hello');

  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (response) {
      // console.log(response);
      $div.text(response.hello);
    }
  });
});
