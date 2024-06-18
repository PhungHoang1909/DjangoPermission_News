from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CompanyLoginForm(AuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username.endswith("@company.vn"):
            raise forms.ValidationError("Email must be @company.vn")
        return username
