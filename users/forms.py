from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(
      label='Username', 
      max_length=100, 
      required=True, 
      widget=forms.TextInput(
        attrs={'class': 'form-control', "placeholder": "Ex.: Jonh Smith"}
      )
    )
    email = forms.EmailField(
      label='Email', 
      required=True,
      widget=forms.EmailInput(
        attrs={'class': 'form-control', "placeholder": "Ex.: john@xpto.com"}
      )
    )
    password = forms.CharField(
      label='Password', 
      widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Type your password here"}), 
      required=True
    )
    password2 = forms.CharField(
      label='Confirm Password', 
      widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Confirm your password"}), 
      required=True
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        max_length=100,
        widget=forms.TextInput(
          attrs={'class': 'form-control', "placeholder": "Ex.: Jonh Smith"}
        ),
        required=True
      )
        
    password = forms.CharField(
        label='Password', 
        max_length=70, 
        widget=forms.PasswordInput(
          attrs={'class': 'form-control', "placeholder": "Type your password here"}
        ), 
        required=True
    )