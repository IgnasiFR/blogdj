from django import forms

#models
from .models import Suscribirse

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


