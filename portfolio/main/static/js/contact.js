// function validate_contact(data) {
//     let errors = {}
//     if (!data.name) {
//         errors.name = "Name is required"
//     }
//     if (!data.email) {
//         errors.email = "Email is required"
//     }
//     if (!data.message) {
//         errors.message = "Message is required"
//     }
//     return errors
// }

document.getElementById("contactForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const response = await fetch("", {  // Empty string means current URL
        method: "POST",
        headers: {
            "X-CSRFToken": formData.get("csrfmiddlewaretoken")
        },
        body: formData
    });

    // const result = await response.json();

    successMessage = document.getElementById("submitSuccessMessage");
    errorMessage = document.getElementById("submitErrorMessage");

    if(response.ok) {
        successMessage.classList.remove("d-none");
        if(!errorMessage.classList.contains("d-none")) {
            console.log("Error message should be hidden.");
            errorMessage.classList.add("d-none");
        }
    } else {
        errorMessage.classList.remove("d-none");
        if(!successMessage.classList.contains("d-none")) {
            console.log("Successs message should be hidden.");
            successMessage.classList.add("d-none");
        };
    }
});