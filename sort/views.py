from pipes import Template
from re import L
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import fileSystem
from django.http import HttpResponse

class Home(TemplateView):
    template_name = 'list_sort.html'
    
def list_sort(request):
    sort = request.GET.get('sort','')
    if sort == 'recent':
        file_list = fileSystem.objects.order_by('created_at', 'created_at')
    elif sort == 'size':
        file_list = fileSystem.objects.order_by('size', 'created_at')
    else:
        file_list = fileSystem.objects.order_by('title', 'created_at')
    return render(request, 'list_result.html', {'file_list': file_list})