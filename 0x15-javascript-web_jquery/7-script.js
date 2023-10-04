//JavaScript script that fetches the character name from this
//URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    $('div#character').text(data.name);
  }
});
