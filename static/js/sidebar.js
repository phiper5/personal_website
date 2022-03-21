$(document).ready(function() {
    sidebarState = $(window).width() >= 1000;
    sidebarResize();
});

$(window).on("resize", function() {
    clearTimeout(window.sidebarTimer);
    window.sidebarTimer = setTimeout(sidebarResize, 500);
});

/* Set the width of the sidebar to 250px and the left margin of the page
 * content to 250px */
function openNav() {
    sidebarState = 1;
    sidebarResize();
}

/* Set the width of the sidebar to 0 and the left margin of the page
 * content to 0 */
function closeNav() {
    sidebarState = 0;
    $("#main-sidebar").css("width", "0");
    $("#main").css("marginLeft", "0");
    $("#main-sidebar").on("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd",
        function(e) {
            $("#main").css("white-space", "normal");
            $(this).off(e);
        });
}

function sidebarResize() {
    if (!sidebarState)
        return;

    if ($(window).width() < 500) {
        width = $(window).width();
    } else {
        width = 250;
    }
    width = width.toString() + "px";
    $("#main-sidebar").css("width", width);
    $("#main").css("margin-left", width);
    $("#main").css("white-space", "nowrap");
}
