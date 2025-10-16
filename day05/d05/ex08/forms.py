from django import forms

class DeleteForm(forms.Form):
    title = forms.ChoiceField(choices=[])
    description = forms.CharField(widget=forms.Textarea)