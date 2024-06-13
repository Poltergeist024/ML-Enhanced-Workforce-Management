document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // prevent the form from submitting normally

    // collect form data
    var formData = new FormData(this);

    // convert form data to JSON
    var jsonData = {};
    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });

    // send data to server
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify(jsonData),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            throw new Error(data.error);
        }
        alert('Form submitted successfully!');
        document.getElementById('myForm').reset(); // reset the form
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Form submission failed: ' + error.message);
    });
});



function validateForm() {
    return validateEmpID() && validateAge() && validateDistanceFromHome() && validateHourlyRate() &&
           validateSalaryHike() && validateTotalWorkExperience() &&
           validateExperienceAtCompany() && validateExperienceInCurrentRole() &&
           validateYearsWithManager();
}

function validateEmpID() {
    const empID = document.getElementById('EmpID').value;
    const errorElement = document.getElementById('empid-error');
    const empIDPattern = /^E\d{7}$/;
    if (!empIDPattern.test(empID)) {
        errorElement.textContent = 'Employee ID must be in the format E followed by 7 digits (e.g., E1003000).';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}


function validateAge() {
    const age = document.getElementById('Age').value;
    const errorElement = document.getElementById('age-error');
    if (age < 18 || age > 75) {
        errorElement.textContent = 'Age must be between 18 and 75.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateDistanceFromHome() {
    const distance = document.getElementById('DistanceFromHome').value;
    const errorElement = document.getElementById('distance-error');
    if (distance < 0 || distance > 40) {
        errorElement.textContent = 'Distance from home must be between 0 and 40 kms.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateHourlyRate() {
    const rate = document.getElementById('EmpHourlyRate').value;
    const errorElement = document.getElementById('hourly-rate-error');
    if (rate < 100 || rate > 5000) {
        errorElement.textContent = 'Hourly rate must be between 100 and 5000.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateSalaryHike() {
    const hike = document.getElementById('EmpLastSalaryHikePercent').value;
    const errorElement = document.getElementById('salary-hike-error');
    if (hike < 11 || hike > 25) {
        errorElement.textContent = 'Salary hike percent must be between 11 and 25.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateTotalWorkExperience() {
    const experience = document.getElementById('TotalWorkExperienceInYears').value;
    const errorElement = document.getElementById('total-work-experience-error');
    if (experience < 0 || experience > 57) {
        errorElement.textContent = 'Total work experience must be between 0 and 57 years.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateExperienceAtCompany() {
    const experienceAtCompany = document.getElementById('ExperienceYearsAtThisCompany').value;
    const totalExperience = document.getElementById('TotalWorkExperienceInYears').value;
    const errorElement = document.getElementById('experience-at-company-error');
    if (experienceAtCompany > totalExperience) {
        errorElement.textContent = 'Experience at this company must be less than or equal to total work experience.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateExperienceInCurrentRole() {
    const experienceInRole = document.getElementById('ExperienceYearsInCurrentRole').value;
    const totalExperience = document.getElementById('TotalWorkExperienceInYears').value;
    const errorElement = document.getElementById('experience-in-role-error');
    if (experienceInRole > totalExperience) {
        errorElement.textContent = 'Experience in current role must be less than or equal to total work experience.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateYearsWithManager() {
    const yearsWithManager = document.getElementById('YearsWithCurrManager').value;
    const experienceAtCompany = document.getElementById('ExperienceYearsAtThisCompany').value;
    const errorElement = document.getElementById('years-with-manager-error');
    if (yearsWithManager > experienceAtCompany) {
        errorElement.textContent = 'Years with current manager must be less than or equal to experience at this company.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}
