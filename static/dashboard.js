document.getElementById("down-btn").addEventListener("click", function() {
    showPopup();
});

document.getElementById("confirmPopup").addEventListener("click", function() {
    showPopup2();
});

document.getElementById("settingsPopup").addEventListener("click", function() {
    showPopup3();
});

document.getElementById("deleteAccount").addEventListener("click", function() {
    showPopup4();
});

document.getElementById("closePopup").addEventListener("click", function() {
    closePopup();
});

document.getElementById("closePopup2").addEventListener("click", function() {
    closePopup2();
});

document.getElementById("closePopup3").addEventListener("click", function() {
    closePopup3();
});

document.getElementById("closePopup4").addEventListener("click", function() {
    closePopup4();
});

document.getElementById("save-btn").addEventListener("click", function() {
    closePopup3();
});

function showPopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "block";
}

function showPopup2() {
    var popup = document.getElementById("popup2");
    popup.style.display = "block";

    var popup = document.getElementById("popup");
    popup.style.display = "none";
}

function showPopup3() {
    var popup = document.getElementById("popup3");
    popup.style.display = "block";
}

function showPopup4() {
    var popup = document.getElementById("popup4");
    popup.style.display = "block";

    var popup = document.getElementById("popup3");
    popup.style.display = "none";
}

function closePopup() {
    var popup = document.getElementById("popup");
    popup.style.display = "none";
}

function closePopup2() {
    var popup = document.getElementById("popup2");
    popup.style.display = "none";
}

function closePopup3() {
    var popup = document.getElementById("popup3");
    popup.style.display = "none";
}

function closePopup4() {
    var popup = document.getElementById("popup4");
    popup.style.display = "none";
}