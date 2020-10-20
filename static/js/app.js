function buildTable() {
  /* data route */
  var url = "/highscore";
  d3.json(url).then(function(response) {

    console.log(response);

    var Username = response.map(p => p.Username);
    var Highscore = response.map(p => p.Score);

    //console.log(pet_name);
    //console.log(pet_type);
    //console.log(pet_age);
    
    var table = d3.select("#highscore-table");
    var tbody = table.select("tbody");
    console.log(tbody);
    var trow;
    for (var i = 0; i < Username.length; i++) {
      trow = tbody.append("tr");
      trow.append("td").text(Username[i]);
      trow.append("td").text(Highscore[i]);
      }
  });
}

buildTable();

