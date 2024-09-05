function validate_contact(data) {
    let errors = {}
    if (!data.name) {
        errors.name = "Name is required"
    }
    if (!data.email) {
        errors.email = "Email is required"
    }
    if (!data.message) {
        errors.message = "Message is required"
    }
    return errors
}

document.getElementById("contactForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const response = await fetch("", {
        method: "POST",
        headers: {
            "X-CSRFToken": formData.get("csrfmiddlewaretoken")
        },
        body: formData
    });

    messageBox = document.getElementById("messageBox");
    if(response.ok) {
        // const result = await response.json();
        // messageBox.innerHTML = `<p>${result.key}: ${result.value}</p>`;
        document.getElementById("submitSuccessMessage").classList.remove("d-none");
    } else {
        // messageBox.innerHTML = `<p>There was an error submitting your message. Please try again.</p>`;
        document.getElementById("submitErrorMessage").classList.remove("d-none");
    }
});