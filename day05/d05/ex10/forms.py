from django import forms

class SearchForm(forms.Form):
    min_date = forms.DateField(label="Movies minimum release date")
    max_date = forms.DateField(label="Movies maximum release date", input_formats=['%Y-%m-%d'])
    planet_diameter = forms.IntegerField(label="Planet diameter greater than")
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'female'), ('hermaphrodite', 'hermaphrodite'), ('n/a', 'n/a'), ('none', None)], label="Character gender ")

    