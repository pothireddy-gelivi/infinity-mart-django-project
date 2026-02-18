from django import forms
from accounts.models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
        
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control' ,
        
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'       

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        
        # Check if email already exists
        if email and Account.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email is already registered. Please use a different email or login."
            )
        
        # Check if phone number already exists (only if provided)
        if phone_number and phone_number.strip():
            phone_number_clean = phone_number.strip()
            cleaned_data['phone_number'] = phone_number_clean
            if Account.objects.filter(phone_number=phone_number_clean).exists():
                raise forms.ValidationError(
                    "This phone number is already registered. Please use a different phone number."
                )
        
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email Address',
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    
        