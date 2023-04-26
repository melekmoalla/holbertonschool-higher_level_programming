$(document).ready(function() {

    // Fetch the movie data from the API
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  
      $.each(data.results, function(index, movie) {
  
        // Create a new list item for each movie and append it to the list
        var listItem = $('<li></li>').text(movie.title);
        $('#list_movies').append(listItem);
  
      });
  
    });
  
  });