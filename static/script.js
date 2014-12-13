jQuery( document ).ready(function( $ ) {
    $("#P23_on").on('click', function() {
        $.post("/switch", {"state":"on"});
    });

    $("#P23_off").on('click', function() {
        $.post("/switch", {"state":"off"});
    });

    $("#dance").on('click', function() {
        $.post("/dance", {"time":".05"});
    });
});