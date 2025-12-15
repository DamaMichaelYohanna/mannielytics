from django import forms
from .models import TeamMember


class TeamMemberForm(forms.ModelForm):
    """Form for creating and updating team members"""
    
    class Meta:
        model = TeamMember
        fields = ['name', 'title', 'bio', 'image', 'linkedin_url', 'portfolio_url', 
                  'website_url', 'cv_url', 'order', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': 'e.g., Dr. John Doe'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': 'e.g., CEO & Founder • System Engineer'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'rows': 8,
                'placeholder': 'Enter the team member\'s biography. Use multiple paragraphs for better formatting.'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'accept': 'image/*'
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': 'https://www.linkedin.com/in/username/'
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': 'https://portfolio.example.com'
            }),
            'website_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': 'https://www.example.com'
            }),
            'cv_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': 'https://example.com/cv.pdf'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-green focus:border-transparent',
                'placeholder': '0'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-brand-green focus:ring-brand-green border-gray-300 rounded'
            }),
        }
