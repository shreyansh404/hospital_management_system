/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

function fetchPatients() {
    fetch('http://127.0.0.1:8943/patient')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Clear existing patients
            patients.length = 0;

            // Map the API response to the patients array
            data.message.forEach(patient => {
                patients.push({
                    id: patient.id,
                    first_name: patient.first_name,
                    last_name: patient.last_name,
                    email: patient.email,
                    phone_number: patient.phone_number,
                    address: patient.address,
                    report_url: patient.report_url || "#" // Handle missing report_url
                });
            });
            updatePatientsTable(patients);
        })
        .catch(error => {
            console.error('Error fetching patients:', error);
            alert('Error fetching patients: ' + error.message);
        });
}

function viewReport(patientId) {
    const apiUrl = `http://127.0.0.1:8943/report/${patientId}`;
    console.error("------------")
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json(); 
        })
        .then(data => {
            console.log('Report Data:', data); 
            alert("Report downloaded successfully!")
            // window.location.href = `/view_report/${patientId}`;
        })
        .catch(error => {
            console.error('Error fetching report:', error);
            alert('Error fetching report. Please try again later.'); 
        });
}

function reportPatient(patientId) {
    window.location.href = '/add_report/' + patientId;
}

function updatePatient(patientId) {
    window.location.href = '/update_patient/' + patientId; 
}
function openUpdateModal(id, firstName, lastName, email, phoneNumber, address) {
    // Populate the modal fields with patient data
    document.getElementById('patientId').value = id;
    document.getElementById('firstName').value = firstName;
    document.getElementById('lastName').value = lastName;
    document.getElementById('email').value = email;
    document.getElementById('phoneNumber').value = phoneNumber;
    document.getElementById('address').value = address;

    // Show the modal
    const modal = new bootstrap.Modal(document.getElementById('updatePatientModal'));
    modal.show();
}

// Handle the form submission
document.getElementById('updatePatientForm').onsubmit = function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);
    // Here you can make an AJAX request to update the patient data
    // For example, using fetch:
    fetch('/update_patient', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('Patient updated successfully!');
            location.reload(); // Reload the page to see changes
        } else {
            alert('Failed to update patient!');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
};