//  List, add, remove without document.querySelector
$(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list').children().last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').children().remove();
  });
});
