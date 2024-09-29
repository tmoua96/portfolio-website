from typing import Any
from .models import Contact
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

    def clean(self) -> dict[str, Any]:
        super(ContactForm, self).clean()

        return self.cleaned_data
    
    def clean_name(self) -> str:
        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError("Name is required")
        elif not re.match(r'^[a-zA-Z\s]+$', name):
            raise forms.ValidationError("Name can only contain letters and spaces")
        
        return name
    
    def clean_email(self) -> str:
        email = self.cleaned_data.get("email")
        if not email:
            raise ValueError("Email is required")
        
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Email is invalid")
        
        return email
    
    def clean_subject(self) -> str:
        subject = self.cleaned_data.get("subject")
        if not subject:
            raise ValueError("Subject is required")
        
        return subject

    def clean_message(self) -> str:
        message = self.cleaned_data.get("message")
        if not message:
            raise ValueError("Message is required")
        
        return message