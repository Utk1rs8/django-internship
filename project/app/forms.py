from django import forms
from .models import Register
class AdminRegistrationsForm(forms.ModelForm):
    corfirm_password = forms.CharField( max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Confirm Password")
    class Meta:
        model = Register
        fields =('name','email','mobile','password')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
