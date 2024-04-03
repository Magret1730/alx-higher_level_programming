$(document).ready(function () {
  const addItem = $('#add_item');
  const removeItem = $('#remove_item');
  const clearList = $('#clear_list');
  const list = $('ul.my_list');

  addItem.on('click', function () {
    list.append('<li>Item</li>');
  });

  removeItem.on('click', function () {
    list.children().last().remove(); // Remove the last child element
  });

  clearList.on('click', function () {
    list.empty(); // Remove all child elements
  });
});
