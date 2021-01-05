var largeScreen = document.getElementById("large-screen");
var largeScreenMenuItem = largeScreen.getElementsByClassName("menu")[0];
var largeScreenSidebar = largeScreen.getElementsByClassName("sidebar")[0];

var smallScreen = document.getElementById("small-screen");
var smallScreenMenuItem = smallScreen.getElementsByClassName("menu")[0];
var smallScreenSidebar = smallScreen.getElementsByClassName("sidebar")[0];

var blogMenuButton = document.getElementById("menu-button");
var prevWindowSize = window.innerWidth;

smallScreenMenuItem.style.display = "none";
largeScreenMenuItem.style.display = "none";

if(window.innerWidth <= 920) {
    smallScreen.style.display = "block";
    largeScreen.style.display = "none";
} else {
    smallScreen.style.display = "none";
    largeScreen.style.display = "inline-flex";
}

function blogOnResize() {
    console.log(smallScreenMenuItem.offsetHeight);
    if(window.innerWidth <= 920) {
        if(prevWindowSize > 920) {
            smallScreenMenuItem.style.display = largeScreenMenuItem.style.display;
            smallScreen.style.display = "block";
            largeScreen.style.display = "none";
        }
    } else if (window.innerWidth > 920) {
        if (prevWindowSize <= 920){
            largeScreenMenuItem.style.display = smallScreenMenuItem.style.display;
            smallScreen.style.display = "none";
            largeScreen.style.display = "inline-flex";
        }
    }
    prevWindowSize = window.innerWidth;
}

blogMenuButton.addEventListener('click', function() {
    if(smallScreen.style.display != "none"){
        if(smallScreenMenuItem.style.display == "none"){
            smallScreenMenuItem.style.display = "inline";
            blogMenuButton.textContent = "◄";
        } else{
            smallScreenMenuItem.style.display = "none";
            blogMenuButton.textContent = "►";
        }
    } else {
        if(largeScreenMenuItem.style.display == "none"){
            largeScreenMenuItem.style.display = "inline";
            blogMenuButton.textContent = "◄";
        } else{
            largeScreenMenuItem.style.display = "none";
            blogMenuButton.textContent = "►";
        }
    }
});