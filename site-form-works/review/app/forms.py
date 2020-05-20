from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    def clean_text(self):
        text = self.cleaned_data['text']
        if text:
            return text
        else:
            raise forms.ValidationError({'text': 'Поле не должно быть пустым'})

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
