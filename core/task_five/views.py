from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import StudentTaskFive

class StudentList(ListView):
    model = StudentTaskFive

class StudentCreate(CreateView):
    model = StudentTaskFive
    fields = ['name','userid','roll_no', 'branch']
    success_url = reverse_lazy('task_five:student_list')

class StudentUpdate(UpdateView):
    model = StudentTaskFive
    fields = ['name','userid','roll_no', 'branch']
    success_url = reverse_lazy('task_five:student_list')

class StudentDelete(DeleteView):
    model = StudentTaskFive
    success_url = reverse_lazy('task_five:student_list')
