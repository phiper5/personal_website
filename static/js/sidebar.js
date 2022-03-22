$(document).ready(function() {
    window.sidebarWidth = 280;
    $("#headshot-picture").css("width",
        (window.sidebarWidth-100).toString()+"px");
    window.sidebarState = $(window).width() >= 1000;
    sidebarResize();
});

$(window).on("resize", function() {
    clearTimeout(window.sidebarTimer);
    window.sidebarTimer = setTimeout(sidebarResize, 200);
});

/* Set the width of the sidebar to 250px and the left margin of the page
 * content to 250px */
function sidebarOpen() {
    window.sidebarState = 1;
    sidebarResize();
}

/* Set the width of the sidebar to 0 and the left margin of the page
 * content to 0 */
function sidebarClose() {
    window.sidebarState = 0;
    $("#main-sidebar").css("width", "0");
    $("#main").css("marginLeft", "0");
}

function sidebarResize() {
    // Skip if the sidebar is off
    if (!window.sidebarState)
        return;

    // Resize the window
    if ($(window).width() < 768) {
        width = $(window).width();
        $("#headshot").css("display", "none");
    } else {
        width = window.sidebarWidth;
        $("#headshot").css("display", "block");
    }
    widthPx = width.toString() + "px";
    $("#main-sidebar").css("width", width);
    $("#main").css("margin-left", width);

    // Resize the sidebar font based on window width
    $("#main-sidebar").find("a").css("font-size", width*0.09);
}
