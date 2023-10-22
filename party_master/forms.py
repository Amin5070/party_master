from django import forms
from party_master.models import PartyMaster


class PartyMasterForm(forms.ModelForm):
    class Meta:
        model = PartyMaster
        fields = "__all__"  # You can specify the fields you want to include here
