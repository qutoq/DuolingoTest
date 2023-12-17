from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'message']
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'rows': 7
                }
            )
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Комментарий', required=True)
    first_name = forms.CharField(required=True, label="Имя")

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
