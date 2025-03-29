from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('donor', 'Donor'),
        ('organization', 'Organization'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)
    license_number = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=255, required=False)
    pin_code = forms.CharField(max_length=10, required=False)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data
