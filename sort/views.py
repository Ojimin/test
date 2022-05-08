from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import list


class Home(TemplateView):
    template_name = 'home.html'


def list_sort(request):
    '''
    sort = request.GET.get('sort', '')
    if sort == 'title':
        content_list = list.objects.all().order_by('-title', '-created_at')
    elif sort == 'size':
        content_list = list.objects.all().order_by('-size', '-created_at')
    elif sort == 'created_at':
        content_list = list.objects.all().order_by('-created_at')
    '''
    sort = request.Get.get('sort', '')
    if sort == 'recent':
        file_list = list.objects.order_by('created_at', 'created_at')
    elif sort == 'size':
        file_list = list.objects.order_by('size', 'created_at')
    elif sort == 'title':
        file_list = list.objects.order_by('title', 'created_at')

    context = {'file_list': file_list}
    return render(request, 'sort/list_sort.html', context)
