$(function () {
  $('#add_item').on('click', function () {
    const newListItem = $('<li>Item</li>');
    $('UL.my_list').append(newListItem);
  });
});
