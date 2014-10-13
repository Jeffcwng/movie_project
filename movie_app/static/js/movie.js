$(document).ready(function(){


    $('#searchmovie').on('click', function () {

        var apikey = "f5reanm8g5md483ajtvst4d3";
        var base_url = "http://api.rottentomatoes.com/api/public/v1.0";
        var movie_name = $("#search").val();
        var search_url = base_url + "/movies.json?apikey=" + apikey + "&q=" + movie_name + "&page_limit=1";
        console.log(search_url);

        $.ajax({
            url: search_url,
            type: "GET",
            dataType: "jsonp",
            success: function(data) {
            console.log(data);
            var movie_poster = data.movies[0].posters.original;


             $('#movie_display').append('<img id="image" width="252px" height="360px" src="' +movie_poster.split("_tmb")[0] + '_ori.jpg"/>' +
                 '<div align="left" style="padding-left: 20px;"><h2>' + data.movies[0].title +
                 '</h2><p>Star: ' + data.movies[0].abridged_cast[0].name +
                 '<br>Release year: '+ data.movies[0].year +
                 '<br>'+ data.movies[0].runtime +' minutes</p></div>');
                $('h2').on('click', function(){

                    alert('watch this');
                 });
                $('img').on('click', function(){

                     window.location = "/profile/";
                 });

             },
             error: function(response) {
                alert("Sorry, we can't find the movie or no such movie!");
             }

        });


    });



});
