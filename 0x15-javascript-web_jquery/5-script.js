$(document).ready(function () {
  const div = $('#add_item');
  const list = $('.my_list');

  div.on('click', function () {
    list.append('<li>Item</li>');
  });
});
