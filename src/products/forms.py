from django import forms

class ProductUploadForm(forms.Form):
    csv_file = forms.FileField(
        label='Select a file',
        help_text='max. 100 megabytes'
    )