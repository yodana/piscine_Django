from django import forms

class DeleteForm(forms.Form):
    title = forms.ChoiceField(choices=[])