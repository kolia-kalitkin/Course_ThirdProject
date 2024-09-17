from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)   # надо создать объект формы и передать форме пришедшие из запроса данные.
        if userform.is_valid():             # проверяем их корректность
            name = userform.cleaned_data['name']
            return HttpResponse(f'<h2>Hello, {name}</h2>')
        else:
            return HttpResponse('Invalid data')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})