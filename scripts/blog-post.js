var menuItem = document.getElementById("menu");
var menuButton = document.getElementById("menu-button");

menuItem.style.display = "none";

menuButton.addEventListener('click', function() {
    if(menuItem.style.display == "none"){
        menuItem.style.display = "inline";
        menuButton.textContent = "◄"
    } else{
        menuItem.style.display = "none";
        menuButton.textContent = "►"
    }
    
});