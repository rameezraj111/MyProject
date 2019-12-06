from django import forms
class ContactForm(forms.Form):
    contact_name=forms.CharField(label='Enter your name',required=True)
    contact_email=forms.EmailField(label='Enter your E-mail',required=True)
    content=forms.CharField(label='Your Message',required=True,widget=forms.Textarea)
