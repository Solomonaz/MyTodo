from django import forms
from .models import Account


class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kargs):
        super(Register, self).__init__(*args, **kargs)
        self.fields['username'].widget.attrs={'placeholder':'User name ...', 'class':'border border-primary border-1 form-control form-control-lg me-3'}
        self.fields['email'].widget.attrs={'placeholder':'Email address','class':'border border-primary form-control-lg text-muted border-1'}
        self.fields['password'].widget.attrs={'placeholder':'password','class':'border border-primary form-control-lg text-muted border-1'}
        self.fields['confirm_password'].widget.attrs={'placeholder':'Confirm password','class':'border border-primary form-control-lg text-muted border-1'}

    def clean(self):
        cleaned_data =  super(Register, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )