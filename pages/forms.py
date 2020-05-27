from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)

