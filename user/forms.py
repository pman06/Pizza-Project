from django import forms
from .models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """A form to create new user, includes all required fields"""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = MyUser
        fields = ['email', 'username', 'first_name', 'last_name']

    def clean_password(self):
        """Check the password entries match"""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password does not match')
        return password2

    def save(self, commit=True):
        """Save provided password in hashed form"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Form for updating users"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_staff'
        ]

        def clean_password(self):
            return self.initial['password']
