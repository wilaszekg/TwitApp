from django.forms.fields import CharField
from django.forms.forms import Form


class LoginForm(Form):
    login = CharField()
    password = CharField()