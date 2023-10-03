function openPopup() {
    var popup = document.getElementById('popup');
    popup.style.display = 'block';
}

function closePopup() {
    var popup = document.getElementById('popup');
    popup.style.display = 'none';
}

function checkBalance() {
    var bal = parseFloat("{{ session['bal'] }}");
    var amount = parseFloat(document.getElementById("amount").value);

    if (bal < amount) {
        // Show the insufficient funds popup
        document.getElementById("insufficient-funds-popup").style.display = "block";
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}