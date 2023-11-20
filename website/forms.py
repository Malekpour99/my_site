from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    # def save(self, commit=True):
    #     instance = super(ContactForm, self).save(commit=False)
    #     instance.name = "Unkown"
    #     if commit:
    #         instance.save()
    #     return instance


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
