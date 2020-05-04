from django import forms


class Email(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
