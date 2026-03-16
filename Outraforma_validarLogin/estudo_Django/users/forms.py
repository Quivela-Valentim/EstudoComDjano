#from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


#class Loginform(forms.ModelForm):
    
 #   class Meta:
 #       model = User 
 #       fields = ['username', 'password']
 #      labels= {'username':'login', 'password':'senha'}

class Loginform(forms.Form):
    login = forms.CharField(max_length=50)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput())
    
    def clean_login(self):
        nome = self.cleaned_data['login']
        if not(nome.isalnum()):
            raise ValidationError("O nome do usuário não pode caractere especial")
        return nome
    
   # def clean_senha(self):
   #     palavraPasse = self.cleaned_data['senha']
    #    if palavraPasse.isalnum():
   #         raise ValidationError("A palavra passe do usuário  deve caractere especial")
    #    return palavraPasse