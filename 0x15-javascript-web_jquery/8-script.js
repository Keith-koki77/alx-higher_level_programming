//JavaScript script that fetches and lists the title for all movies
//by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    $.each(data.results, function (index, movie) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
