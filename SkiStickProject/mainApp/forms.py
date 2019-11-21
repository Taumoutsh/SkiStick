from django import forms

class ComentarioForm(forms.Form):
    calificacion = forms.IntegerField(label='Da tu calificacion de la estacion (sobre 5) ')
    comentario = forms.CharField(label='Tus comentarios ', widget=forms.Textarea)

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Tu usuario nombre ')
    contrasena = forms.CharField(label='Tu contrasena ')