from django import forms

from .models import Package, Category, Comment
from profiles.models import User

class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['package', 'text']
        widgets = {
            'package': forms.HiddenInput(),
            'text': forms.Textarea(attrs={'placeholder': 'Write your comment/review here...'})
        }
