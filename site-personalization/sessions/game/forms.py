from django import forms

from .models import PlayerGameInfo


class GameForm(forms.Form):
    number = forms.IntegerField(max_value=100, min_value=0, label='Введите число ')

    def clean_number(self):
        number = int(self.cleaned_data['number'])
        if -1 < number < 101:
            return number
        else:
            raise forms.ValidationError('Ошибка')

    class Meta(object):
        model = PlayerGameInfo
        exclude = ('player', 'game')
