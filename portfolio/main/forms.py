from typing import Any
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

    def clean(self) -> dict[str, Any]:
        super(ContactForm, self).clean()
        
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        subject = self.cleaned_data.get("subject")
        message = self.cleaned_data.get("message")

        if not name:
            self._errors["name"] = self.error_class(["Name is required"])
        if not email:
            self._errors["email"] = self.error_class(["Email is required"])
        if not subject:
            self._errors["subject"] = self.error_class(["Subject is required"])
        if not message:
            self._errors["message"] = self.error_class(["Message is required"])

        return self.cleaned_data
    