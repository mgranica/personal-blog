from django import forms

from .models import Subcriber, Contact

class SubcriberForm(forms.ModelForm):
    class Meta:
        model = Subcriber
        fields = (
            'email',
        )
        widget = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': ' Email...',
                }
            )
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
