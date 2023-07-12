from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee

INDEX_TEMPLATE = 'app/index.html'

def home(request):
    return render(request, INDEX_TEMPLATE)

class EmployeeListView(ListView):
    model = Employee
    template_name = INDEX_TEMPLATE
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = INDEX_TEMPLATE
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = INDEX_TEMPLATE
    fields = ['name', 'email', 'department', 'position', 'start_date']

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = INDEX_TEMPLATE
    fields = ['name', 'email', 'department', 'position', 'start_date']

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = INDEX_TEMPLATE
    success_url = '/myapp/'
