from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserFrom(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
