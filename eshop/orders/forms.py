from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'contact_form_name input_field', 
		'placeholder': ('First Name')}))
	last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'contact_form_name input_field', 
		'placeholder': ('Last Name')}))
	email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'contact_form_email input_field', 
		'placeholder': ('Email Address')}))
	address = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'text_field contact_form_message', 
		'placeholder': ('House Address')}))
	postal_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'contact_form_phone input_field', 
		'placeholder': ('Postal code')}))
	city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'contact_form_name input_field', 
		'placeholder': ('City')}))
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
