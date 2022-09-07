from django.forms import ModelForm
from .models import ApprovalToConfirm


class ApprovalForm(ModelForm):
    class Meta:
        model = ApprovalToConfirm
        fields = ['image', 'description', 'is_approved', 'user', 'value']
