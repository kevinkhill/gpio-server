jQuery( document ).ready(function( $ ) {
    $("#P23_on").on('click', function() {
        $.post("/switch", {"state":"on"});
    });

    $("#P23_off").on('click', function() {
        $.post("/switch", {"state":"off"});
    });

    $("#flicker").on('click', function() {
        $.post("/flicker", {"time":".05"});
    });

    $("#midi").on('click', function() {
        $.post("/midi", {"filename":"for_whom_the_bell_tolls.mid"});
    });
});