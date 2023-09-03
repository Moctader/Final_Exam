from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
from .models import UserAccount, User_Address


class RegistrationForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username', 'password1', 'password2','first_name', 
                'last_name','email','birth_date', 'postal_code', 'country']

    def save(self, commit=True):
        our_user=super().save(commit=False)
        if commit==True:
            our_user.save()
            gender=self.cleaned_data.get('gender')
            country=self.cleaned_data.get('country')
            birth_date=self.cleaned_data.get('birth_date')
            postal_code=self.cleaned_data.get('postal_code')

            User_Address.objects.create(
                user=our_user,
                postal_code=postal_code,
                country=country     
            )
            UserAccount.objects.create(
                user=our_user,
                birth_date=birth_date,
                gender=gender,                
            )
        return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
            
            
class UpadateForm(forms.ModelForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email']

  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
        if self.instance:
            try:
                user_account=self.instance.account
                user_Address=self.instance.address
            except UserAccount.DoesNotExist:
                user_account=None
                user_Address=None
                
            if user_account:
                self.fields['birth_date'].initial=user_account.birth_date
                self.fields['gender'].initial=user_account.gender
                self.fields['postal_code'].initial=user_Address.postal_code
                self.fields['country'].initial=user_Address.country
        
        def save(self, commit=True):
            user=super().save(commit=False)
        
            if commit==True:
                user.save()
                
                user_account, created=UserAccount.objects.get_or_create(user=user)
                user_Address, created=User_Address.objects.get_or_create(user=user)
                
                user_account.gender=self.cleaned_data.get('gender')
                user_account.birth_date=self.cleaned_data.get('birth_date')
                user_account.save()
                
                user_Address.country=self.cleaned_data.get('country')
                user_Address.postal_code=self.cleaned_data.get('postal_code')
                user_Address.save()
                
            return user
