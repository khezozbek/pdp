from django.shortcuts import render, redirect

from .models import Speciality, Subject, Teacher
from .forms import SpecialityForm, TeacherForm


def sub_detail(requset, pk):
    sub = Subject.objects.get(pk=pk)
    return render(requset, 'render/subject/det_sub.html', {
        'subject': sub,
    })


def sub_lis(request):
    sub = Subject.objects.all()
    return render(request, 'render/subject/index.html', {
        'sub': sub,
    })


def spec_detail(request, pk):
    spec = Speciality.objects.get(pk=pk)
    return render(request, 'render/detail.html', {
        'spec': spec,
    })


def spec_list(request):
    search = request.GET.get(request, 'search')
    if search:
        spec = Speciality.objects.filter(name__contains=search)
    else:
        spec = Speciality.objects.all()

    return render(request, 'render/index.html', {
        'spec': spec, 'search': search,
    })


def spec_create(request):
    if request.method == "GET":
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cret = Speciality.objects.create(
                name=data['name'],
                code=data['code'],
                start_data=data['start_data'],
                is_activate=data['is_activate'],
            )
            return redirect("spec-list")

    return render(request, "render/spec_create/create.html", {
        "form": form,
    })


def teach_detail(request, pk):
    teach = Teacher.objects.get(pk=pk)
    return render(request, "render/teacher_creat/teacher_detail.html", {
        "teacher": teach
    })


def teach_list(request):
    teach = Teacher.objects.all()
    return render(request, 'render/teacher_creat/teacher.html', {
        "teacher": teach
    })


def teacher_create(request):
    if request.method == "GET":
        form = TeacherForm()
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("teach-list")
    contex = {"form": form}
    return render(request, "render/spec_create/create.html", contex)


from.models import Subject
from.forms import SubjectForm


def subject_create(requset):
    if requset.method == "GET":
        form = SubjectForm()
    else:
        form = SubjectForm(requset.POST)
        if form.is_valid():
            form.save()
        return redirect("sub-list")
    context = {"form": form}
    return render(requset, "render/subject/create/create_subject.html", context)
