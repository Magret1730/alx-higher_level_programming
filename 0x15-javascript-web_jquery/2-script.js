$(document).ready(function () {
  const header = $('header');
  const div = $('#red_header');

  div.on('click', function () {
    if (header) {
      header.css('color', '#FF0000');
    }
  });
});
