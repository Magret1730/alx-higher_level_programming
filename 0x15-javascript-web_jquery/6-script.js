$(document).ready(function () {
  const div = $('#update_header');
  const header = $('header');

  div.on('click', function () {
    if (header) {
      header.text('New Header!!!');
    } else {
      console.log('No header');
    }
  });
});
