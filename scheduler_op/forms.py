from django import forms

METHOD_CHOICE = (
    (0,'Hill Climbing'),
    (1,'Simulated Annealing'),
    (2,'Genetic Algorithm'),
    )

class UploadFileForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

    radiobutton = forms.ChoiceField(choices=METHOD_CHOICE,widget=forms.RadioSelect(),label='Select Method')