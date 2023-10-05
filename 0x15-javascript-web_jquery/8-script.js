$(function () {
  const listMovies = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (results) {
      $.each(results, function (i, result) {
        const title = result.title;
        const listItem = $('<li>').text(title);
        listMovies.append(listItem);
      });
    }
  });
});
