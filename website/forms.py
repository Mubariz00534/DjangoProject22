from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-controll', 'placeholder': 'Fullname'}))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-controll', 'placeholder': 'Email'}))

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-controll', 'placeholder': 'Enter Information'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        print(self.cleaned_data)
        if not "gmail.com" in email:
            raise forms.ValidationError("Bu email gmail deyil")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Fullname'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Passowrd',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))

    # def clean_password(self):
    #     data = self.cleaned_data
    #     print(self.cleaned_data)
    #     password = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('password2')
    #     # print(password)
    #     # print(password2)

    #     if password != password2:
    #         raise forms.ValidationError("Bu passwordler eyni deyil")

    #     return data

    def clean_username(self):
        username = self.cleaned_data.get("username")

        qs = User.objects.filter(username=username)

        if qs:
            raise forms.ValidationError("Bele bir user artiq var.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)

        if qs:
            raise forms.ValidationError("Bele bir email var")

        return email