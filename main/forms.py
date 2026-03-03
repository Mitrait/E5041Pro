from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': '9754D50@ya.com'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'placeholder': '02 0234 4 0619'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'placeholder': 'Neue Haas Grotesk Thin', 'rows': 5}))

    def send_email(self):
        send_mail(
            'Новая заявка с E5041.pro',
            f"Email: {self.cleaned_data['email']}\nPhone: {self.cleaned_data['phone']}\nMessage: {self.cleaned_data['message']}",
            'from@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )