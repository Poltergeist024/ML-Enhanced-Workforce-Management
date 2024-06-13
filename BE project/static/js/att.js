
function validateAge() {
    const age = parseInt(document.getElementById('Age').value, 10);
    const errorElement = document.getElementById('age-error');
    if (isNaN(age) || age < 18 || age > 75) {
        errorElement.textContent = 'Age must be between 18 and 75.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateDistanceFromHome() {
    const distance = parseInt(document.getElementById('DistanceFromHome').value, 10);
    const errorElement = document.getElementById('distance-error');
    if (isNaN(distance) || distance < 0 || distance > 40) {
        errorElement.textContent = 'Distance from Home must be between 0 and 40.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateHourlyRate() {
    const hourlyRate = parseInt(document.getElementById('HourlyRate').value, 10);
    const errorElement = document.getElementById('hourlyrate-error');
    if (isNaN(hourlyRate) || hourlyRate < 100 || hourlyRate > 5000) {
        errorElement.textContent = 'Hourly Rate must be between 100 and 5000.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateSalaryHike() {
    const hike = parseInt(document.getElementById('EmpLastSalaryHikePercent').value, 10);
    const errorElement = document.getElementById('hike-error');
    if (isNaN(hike) || hike < 11 || hike > 25) {
        errorElement.textContent = 'Last Salary Hike Percent must be between 11 and 25.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateTotalWorkExperience() {
    const experience = parseInt(document.getElementById('TotalWorkExperienceInYears').value, 10);
    const errorElement = document.getElementById('experience-error');
    if (isNaN(experience) || experience < 0 || experience > 57) {
        errorElement.textContent = 'Total Work Experience In Years must be between 0 and 57.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateExperienceAtCompany() {
    const companyEx = parseInt(document.getElementById('ExperienceYearsAtThisCompany').value, 10);
    const totalEx = parseInt(document.getElementById('TotalWorkExperienceInYears').value, 10);
    const errorElement = document.getElementById('companyex-error');
    if (isNaN(companyEx) || companyEx > totalEx) {
        errorElement.textContent = 'Experience Years At This Company must be less than or equal to Total Work Experience In Years.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateExperienceInCurrentRole() {
    const roleEx = parseInt(document.getElementById('ExperienceYearsInCurrentRole').value, 10);
    const totalEx = parseInt(document.getElementById('TotalWorkExperienceInYears').value, 10);
    const errorElement = document.getElementById('roleex-error');
    if (isNaN(roleEx) || roleEx > totalEx) {
        errorElement.textContent = 'Experience Years In Current Role must be less than or equal to Total Work Experience In Years.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateYearsWithManager() {
    const managerYears = parseInt(document.getElementById('YearsWithCurrentManager').value, 10);
    const companyEx = parseInt(document.getElementById('ExperienceYearsAtThisCompany').value, 10);
    const errorElement = document.getElementById('manager-error');
    if (isNaN(managerYears) || managerYears > companyEx) {
        errorElement.textContent = 'Years With Current Manager must be less than or equal to Experience Years At This Company.';
        return false;
    } else {
        errorElement.textContent = '';
        return true;
    }
}

function validateForm() {
    return validateAge() && validateDistanceFromHome() && validateSalaryHike() &&
           validateTotalWorkExperience() && validateExperienceAtCompany() &&
           validateExperienceInCurrentRole() && validateYearsWithManager();
}

document.getElementById('myForm').addEventListener('submit', function(event) {
    if (!validateForm()) {
        event.preventDefault();
    }
});
