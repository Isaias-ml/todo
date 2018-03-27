from django import forms

from .models import Categoria, Tarefa


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ('user',)


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
