

function validateEmail() {
    var email = document.forms[0]["email"].value;
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var emailError = document.getElementById("email-error");

    if (!emailPattern.test(email)) {
        emailError.textContent = "Please enter a valid email address.";
        return false;
    } else {
        emailError.textContent = "";
        return true;
    }
}

function validateAge() {
    var age = document.forms[0]["age"].value;
    var agePattern = /^(?:1[89]|[2-6][0-9]|70)$/;
    var ageError = document.getElementById("age-error");

    if (!agePattern.test(age)) {
        ageError.textContent = "Please enter a valid age between 18 and 70.";
        return false;
    } else {
        ageError.textContent = "";
        return true;
    }
}

function validateContact() {
    var num = document.forms[0]["num"].value;
    var numPattern = /^\d{10}$/;
    var contactError = document.getElementById("contact-error");

    if (!numPattern.test(num)) {
        contactError.textContent = "Please enter a valid 10-digit contact number.";
        return false;
    } else {
        contactError.textContent = "";
        return true;
    }
}

function validatePassword() {
    var password = document.forms[0]["password"].value;
    var passwordPattern = /^(?=.*\d).{6,}$/;
    var passwordError = document.getElementById("password-error");

    if (!passwordPattern.test(password)) {
        passwordError.textContent = "Password must be at least 6 characters long and include a number.";
        return false;
    } else {
        passwordError.textContent = "";
        return true;
    }
}

function validateForm() {
    var isEmailValid = validateEmail();
    var isAgeValid = validateAge();
    var isContactValid = validateContact();
    var isPasswordValid = validatePassword();

    return isEmailValid && isAgeValid && isContactValid && isPasswordValid;
}
