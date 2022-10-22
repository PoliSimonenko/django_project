from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['nd', 'ndf', '123'],
        'obj': {
            'car': 'BMW',
            'age': 14,
            'hobby': 'kdkd'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')