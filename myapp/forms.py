from django.forms import ModelForm
from .models import Approval


class ApprovalForm(ModelForm):
    class Meta:
        model = Approval
        fields = ['image','description','is_approved','user','value']
      
