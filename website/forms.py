from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))



class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obligatoire. 150 characteres maximum. Lettres, chiffres et @/./+/-/_ seulement.</small></span>'

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Votre password ne peut pas etre une information personnelle.</li><li>Votre password doit contenir au moins 8 characters.</li><li>Votre password ne peut pas etre une password commun.</li><li>Votre password ne peut pas etre juste numerique.</li></ul>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirmez la Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrez la meme password, pour verification.</small></span>'	


# Formulaire pour creer un registre
    
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class":"form-control"}), label="")
    adress = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Adress", "class":"form-control"}), label="")


    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'email', 'adress')

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)


        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''


        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''

        self.fields['adress'].widget.attrs['class'] = 'form-control'
        self.fields['adress'].widget.attrs['placeholder'] = 'Adress'
        self.fields['adress'].label = ''