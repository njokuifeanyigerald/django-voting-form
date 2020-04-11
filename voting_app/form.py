from django import forms
from .models import Vote

class VotingForm(forms.Form):
    chosen_association_options = forms.MultipleChoiceField(choices=[], label="Book Name", required=False,
        widget=forms.SelectMultiple(attrs={
        'class': "form-control"
    }))
    
    other_association_name = forms.CharField(label="other", max_length=100, required=False, widget=(forms.TextInput
    (attrs={
        'class': "form-control",
        'placeholder': "did i miss something?"
    })))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_association_names = Vote.objects.order_by('association_name').values_list('association_name', flat=True).distinct()
        self.fields['chosen_association_options'].choices = [(association_name,association_name)for association_name in unique_association_names]