from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField(
        label='Select Photo',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
            'id': 'image-file-input',
            'onchange': 'previewImage(event)'
        })
    )
    name = forms.CharField(
        max_length=60,
        label='Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter image title (max 60 chars)'
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write a short story or description about this image...'
        })
    )
    author = forms.CharField(
        max_length=40,
        label='Author',
        initial='Anonymous',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name or handle'
        })
    )
    category = forms.CharField(
        max_length=50,
        label='Category',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., Nature, Travel, Architecture'
        })
    )
    location = forms.CharField(
        max_length=60,
        label='Location',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., Tokyo, Paris, Nairobi'
        })
    )
