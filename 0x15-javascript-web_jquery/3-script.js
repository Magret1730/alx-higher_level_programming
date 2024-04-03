$(document).ready(function () {
  const header = $('Header');
  const div = $('#red_header');

  div.on('click', function () {
    if (header) {
      header.addClass('red');
    }
  });
});
