from django import forms
from salles.models import Formation



class FormationForm(forms.ModelForm):
	model = Formation

	class Meta:
		pass