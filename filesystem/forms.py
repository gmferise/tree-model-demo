from django import forms

class CreateFileForm(forms.Form):
    name = forms.CharField(max_length=128)
    is_file = forms.BooleanField(required=False, widget=forms.widgets.HiddenInput)

    def clean(self):
        self.cleaned_data['is_file'] = True
        return self.cleaned_data

class CreateFolderForm(forms.Form):
    name = forms.CharField(max_length=128)
    is_file = forms.BooleanField(required=False, widget=forms.widgets.HiddenInput)

    def clean(self):
        self.cleaned_data['is_file'] = False
        return self.cleaned_data