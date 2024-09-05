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

export default validate_contact;