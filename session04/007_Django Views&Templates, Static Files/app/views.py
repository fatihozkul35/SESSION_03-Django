from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print(request.META)
    return HttpResponse("<h1>Hello World!</h1>")


def blog(request):
    # students = Student.objects.all()
    context = {
        # 'students': students,
        'isim': 'Fatih',
        'soyisim': 'Özkul',
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4],
    }
    return render(request, 'app/index.html', context)
