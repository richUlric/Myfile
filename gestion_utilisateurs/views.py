from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


@login_required
def my_view(request):
    # Code pour la vue ici
    return render(request, 'my_template.html', context)

# Create your views here.from django import forms

class CustomUserCreationForm(UserCreationForm):
    #email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        

def index(request):
    """View function for home page of site."""


    context = {
      
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

