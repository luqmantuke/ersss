from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    subject = forms.CharField(max_length=400)
    phone = forms.CharField(max_length=400)
    message = forms.CharField(widget=forms.Textarea)

