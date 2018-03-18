from django import forms
from django.contrib.auth.models import User
from account.models import UserProfileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('mobile_number',)

    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        self.fields['mobile_number'].widget.attrs.update({'class' : 'form-control'})
