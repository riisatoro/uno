from django.forms import ModelForm, CharField, PasswordInput
from django.core.exceptions import ValidationError

from models.models import CustomUser


class UserCreationForm(ModelForm):
    username = CharField(label="Username")
    password1 = CharField(label="Password", widget=PasswordInput)
    password2 = CharField(label="Password confirmation", widget=PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "username")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
