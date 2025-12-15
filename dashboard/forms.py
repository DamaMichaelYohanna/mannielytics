from django import forms
from django.contrib.auth.forms import AuthenticationForm

class StyledAuthenticationForm(AuthenticationForm):
    """Custom authentication form with styled input fields"""
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-50 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-brand-green focus:border-transparent transition duration-200',
            'placeholder': 'Enter your username',
            'id': 'username'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-50 text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-brand-green focus:border-transparent transition duration-200',
            'placeholder': 'Enter your password',
            'id': 'password'
        })
    )
