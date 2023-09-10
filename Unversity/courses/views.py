from django.shortcuts import render
from .models import Teacher


def teach_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'library/teacher.html', {
        'teacher': teacher,
    })


def teach_list(request):
    search = request.GET.get('search')

    if search:

        teach = Teacher.objects.filter(name__contains=search)
    else:
        teach = Teacher.objects.all()

    return render(request, 'library/home.html', {
        "teach": teach, 'search': search,
    })
