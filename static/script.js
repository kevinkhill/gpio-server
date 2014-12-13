jQuery( document ).ready(function( $ ) {
    $("#P17").on('click', function() {
        $.post("/switch", {"pin":17, "state":"on"}, function (data) {
            console.log(data);
        });
    });

    $("#P18").on('click', function() {
        $.post("/switch", {"pin":18, "state":"on"}, function (data) {
            console.log(data);
        });
    });

    $("#P23_on").on('click', function() {
        $.post("/switch", {"pin":23, "state":"on"}, function (data) {
            console.log(data);
        });
    });

    $("#P23_off").on('click', function() {
        $.post("/switch", {"pin":23, "state":"off"}, function (data) {
            console.log(data);
        });
    });
});