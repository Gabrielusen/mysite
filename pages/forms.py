from django import forms


class Email(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email
