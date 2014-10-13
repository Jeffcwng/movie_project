$(document).ready(function() {


//$.ajax({
//    url: '/all_pokemon',
//    type: "GET",
//    success: function(data) {
//        console.log(data);
//    }
//});


//      paint.js

$.ajax({
    url: '/paint',
    type: "GET",
    success: function(data) {
        console.log(data);
        $('#window_paint').html(data)
    }
});


//      paint.js

$.ajax({
    url: '/snake',
    type: "GET",
    success: function(data) {
        console.log(data);
        $('#window_snake').html(data)
    }
});






});