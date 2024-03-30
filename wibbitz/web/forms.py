from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput, Select
from web.models import Contact
from web.models import COMPANY_SIZE, INDUSTRY, Job_Role ,COUNTRY


EMPTY_COMPANY_SIZE = (("", "Company Size"),) + COMPANY_SIZE
EMPTY_INDUSTRY = (("", "Industry "),) + INDUSTRY
EMPTY_Job_Role = (("", "Job Role "),) + Job_Role
EMPTY_COUNTRY = (("", "Country "),) + COUNTRY


class ContactForm(ModelForm):
    company_size = forms.ChoiceField(choices=EMPTY_COMPANY_SIZE)
    industry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job_role = forms.ChoiceField(choices=EMPTY_Job_Role)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email": EmailInput(attrs={"placeholder": "Enter your email "}),
            "first_name": TextInput(attrs={"placeholder": "Enter your first name "}),
            "last_name": TextInput(attrs={"placeholder": "Enter your last name "}),
            "company": TextInput(attrs={"placeholder": "Enter your company "}),
        }