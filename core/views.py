from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from todo.tarefas.models import Tarefa


@login_required
def home(request):
    tarefas = Tarefa.objects.filter(user=request.user)
    return render(request, 'core/index.html', {'tarefas': tarefas})
