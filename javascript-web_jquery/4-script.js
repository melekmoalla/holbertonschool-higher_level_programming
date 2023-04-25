#!/usr/bin/node

$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
