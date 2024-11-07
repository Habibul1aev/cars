from django import forms
from cars.models import Cars, Category, Hesh
import re
from django.core.exceptions import ValidationError
        
class CarCreate(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'photo', 'volume', 'model', 'info', 'price', 'category', 'teg', 'is_publish']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Название', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}), 
            'volume': forms.TextInput(attrs={'placeholder':'Объем', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}),
            'model': forms.TextInput(attrs={'placeholder':'Модель', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}),
            'info': forms.Textarea(attrs={'placeholder':'Write....', 'class':'mb-2 border outline-none flex'}),
            'price': forms.TextInput(attrs={'placeholder':'Цена', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}),
        }

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if re.match(r'\d', name):
    #         raise ValidationError('Название не далжно начинаться с цифры')
    #     return name
        
