from django import forms

class ComentarioForm(forms.Form):
    calificacion = forms.IntegerField(label='Da tu calificacion de la estacion (sobre 5) ')
    comentario = forms.CharField(label='Tus comentarios ', widget=forms.Textarea)

class LoginForm(forms.Form):
    usuario = forms.CharField()
    contrasena = forms.CharField()

class SigninForm(forms.Form):
    nombre = forms.CharField(label='Tu nombre ')
    apellido = forms.CharField(label='Tu apellido ')
    usuario = forms.CharField(label='Tu usuario nombre ')
    email = forms.EmailField(label='Tu direccion de correo ')
    contrasena = forms.CharField(label='Tu contrasena ', widget=forms.PasswordInput)