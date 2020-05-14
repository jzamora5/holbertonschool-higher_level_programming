$(document).ready(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
});

$(document).ready(() => {
  $('DIV#remove_item').click(() => {
    $('UL.my_list>li:last-child').remove();
  });
});

$(document).ready(() => {
  $('DIV#clear_list').click(() => {
    $('UL.my_list>li').remove();
  });
});
