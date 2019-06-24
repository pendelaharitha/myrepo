from django import forms
from .models import Employee
class CreateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
class updateform(forms.Form):
    username=forms.CharField(
        label="Enter your username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )
    newpassword = forms.CharField(
        label="Enter your newpassword",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'newpassword'
            }
        )
    )
class Deleteform(forms.Form):
    mobile = forms.IntegerField(
        label="Enter your mobilenumber",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'mobilenumber'
            }
        )
    )




