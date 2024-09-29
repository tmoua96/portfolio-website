document.getElementById("name").addEventListener("input", async function(event) {
    this.value = this.value.replace(/[^a-zA-Z\s]/g, "");
    if (this.value.length > 30) {
        this.value = this.value.slice(0, 30);
    }
});

document.getElementById("email").addEventListener("input", async function(event) {
    this.value = this.value.replace(/[^a-zA-Z0-9._%+-@]/g, "");
    if (this.value.length > 50) {
        this.value = this.value.slice(0, 50);
    }
});

document.getElementById("subject").addEventListener("input", async function(event) {
    if (this.value.length > 50) {
        this.value = this.value.slice(0, 50);
    }
});

document.getElementById("contact-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    // TODO: add more interactive validation
    // Add some loading maybe?
    // Add some validation message/popups for other input fields

    try {
        document.getElementById("submit-container").classList.remove("d-none");
        const submitMessage = document.getElementById("submit-message");
        const submitButton = document.getElementById("submit-button");
        submitButton.disabled = true;

        const formData = new FormData(this);
        const response = await fetch("", {  // Empty string means current URL
            method: "POST",
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken")
            },
            body: formData
        });

        const result = await response.json();

        if(response.ok) {
            // Set as array incase more classes are added. Can probably just make it a single
            const successClasses = ["text-success"];

            submitMessage.textContent = result["message"];
            
            if(submitMessage.classList.contains("text-danger")) {
                submitMessage.classList.remove("text-danger");
            }
            successClasses.forEach(c => submitMessage.classList.add(c));
        } else {
            displayErrorMessage(result["message"], submitMessage);
            submitButton.disabled = false;
        }
    } catch (error) {
        submitButton.disabled = false;
        displayErrorMessage(error, submitMessage);
        console.error(error, error.body);
    }

    function displayErrorMessage(message, submitMessage) {
        const errorClasses = ["text-danger"];
    
        submitMessage.textContent = message;
        
        if(submitMessage.classList.contains("text-success")) {
            submitMessage.classList.remove("text-success");
        }
        errorClasses.forEach(c => submitMessage.classList.add(c));
    }
});
