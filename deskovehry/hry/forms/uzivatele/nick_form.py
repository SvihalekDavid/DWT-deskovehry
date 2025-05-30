from django import forms

class NickForm(forms.Form):
    username = forms.CharField(label='Oslovuj mě', max_length=10)
