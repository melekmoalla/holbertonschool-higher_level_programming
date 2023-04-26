#!/usr/bin/node

$(document).ready(function () {
  // Fetch the character data from the API
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    // Get the character name from the data and insert it into the HTML
    $('#character').text(data.name);
  });
});
