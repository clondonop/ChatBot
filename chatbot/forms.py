from django import forms

class ChatBotForm(forms.Form):
    message = forms.CharField(
        label="",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Escribe tu mensaje...',
                'class': 'msger-input',
                'id': 'textInput',
            }
        )
    )