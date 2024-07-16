from django import forms

from apps.gallery.models import Pictures

class PictureForm(forms.ModelForm):
    class Meta:
        model = Pictures
        exclude = ['published',]
        labels = {
            'title': 'Title',
            'font': 'Font',
            'category': 'Category',
            'description': 'Description',
            'image': 'Image',
            'published_at': 'Added at',
            'user': 'User',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ex.: Sunset"}),
            'font': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Ex.: A beautiful sunset"}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'published_at': forms.DateTimeInput(
                format='%d-%m-%Y',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }