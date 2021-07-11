from django import forms
from .models import myrecord

class fileform(forms.ModelForm):
    class Meta:
        model=myrecord
        fields=('hospitalname','prescription','doctorname','hospitallocation','diseasename','documentname','file','description')
