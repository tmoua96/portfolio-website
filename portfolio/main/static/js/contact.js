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

    if(response.ok) {
        // document.getElementById("submitSuccessMessage").textContent = result.message;
        document.getElementById("submitSuccessMessage").classList.remove("d-none");
    } else {
        // document.getElementById("submitErrorMessage").textContent = result.message;
        document.getElementById("submitErrorMessage").classList.remove("d-none");
    }
});