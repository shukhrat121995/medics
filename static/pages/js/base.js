$(document).ready(function () {
    var path = window.location.href;
    $(".links").each(function () {
        if (this.href === path) {
            $(this).addClass("active");
        }
        //$(".links").removeClass("active");
        // $(".tab").addClass("active"); // instead of this do the below

    });
});