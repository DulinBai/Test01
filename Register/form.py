from django import forms
from Register.models import User

class RegisterFrom(forms.Form):
    '''
    class Meta:
        model = User
        fields = '__all__'
    '''
    id_num = forms.CharField(max_length=50)
    password_based = forms.CharField(widget=forms.PasswordInput())