from django import forms
from django.contrib.auth.forms import AuthenticationForm

from main.models import News, Author


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={'class': 'form-control'})


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
