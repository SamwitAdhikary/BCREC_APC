from home.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserFrom(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = [
            'name', 'phone_number', 'college_name', 'state', 'bio', 'portfolio_site', 'upload_cv', 'course', 'Semester'
        ]

        # fields = '__all__'


class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = [
            'profile_pic'
        ]
