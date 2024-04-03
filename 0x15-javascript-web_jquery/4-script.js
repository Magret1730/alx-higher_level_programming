$(document).ready(function () {
  const header = $('header');
  const div = $('#toggle_header');

  div.on('click', function () {
    if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    } else {
      header.removeClass('red').addClass('green');
    }
  });
});
