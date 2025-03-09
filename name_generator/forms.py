# name_generator/forms.py
from django import forms

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

NAME_STYLE_CHOICES = [
    ('classic', 'Classic'),
    ('modern', 'Modern'),
    ('trendy', 'Trendy'),
    ('royal', 'Royal'),
    ('unique', 'Unique'),
]

RELIGION_CHOICES = [
    ('muslim', 'Muslim'),
    ('christian', 'Christian'),
    ('neutral', 'Neutral'),
]

class BabyNameForm(forms.Form):
    father_name = forms.CharField(
        label="Father's Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father\'s name'})
    )
    mother_name = forms.CharField(
        label="Mother's Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother\'s name'})
    )
    siblings = forms.CharField(
        label="Siblings' Names (Optional)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sibling names separated by commas'})
    )
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'})
    )
    language = forms.CharField(
        label="Language",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter language'})
    )
    name_style = forms.ChoiceField(
        choices=NAME_STYLE_CHOICES,
        label="Preferred Style",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    religion = forms.ChoiceField(
        choices=RELIGION_CHOICES,
        label="Religion",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label="Baby's Gender",
        widget=forms.Select(attrs={'class': 'form-select'})
    )