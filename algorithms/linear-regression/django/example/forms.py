from django import forms
from .models import LinearRegressionModel


class LinearRegressionForm(forms.ModelForm):
    class Meta:
        model = LinearRegressionModel
        fields = ('x', 'y')
