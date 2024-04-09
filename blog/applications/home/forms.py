from django import forms

#models
from .models import Suscribirse,Contact

class SuscribirseForm(forms.ModelForm):

    class Meta:
        model = Suscribirse
        fields = (
            'email',
        )

        widgets = {

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico...',
                }
            )

        }


class ContactForm(forms.ModelForm):
        class Meta:
             model = Contact
             fields=('__all__')
        



