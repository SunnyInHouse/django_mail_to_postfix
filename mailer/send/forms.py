from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    send_from = forms.EmailField()
    subject = forms.CharField(max_length=55)
    message = forms.CharField(widget=forms.Textarea)
