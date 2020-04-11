
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .forms import NewProcessForm

from sms_app.models import Element, Process, Kpi


# Create your views here.

def home(req):
    elements = Element.objects.all()
    return render(req, "home.html", {"elements":elements})

def element_processes(req, pk):
    element = get_object_or_404(Element, pk=pk)
    context = {'element': element}
    return render(req, "process.html", context)

def new_process(req, pk):
    element = get_object_or_404(Element, pk=pk)

    if req.method == 'POST':
        process_name = req.POST['process_name']
        kpi_name = req.POST['kpi_name']

        user =  User.objects.first() #TODO: get the currently loggedin user

        process = Process.objects.create(
            process_name = process_name,
            element = element,
            created_by = user
        )

        kpi = Kpi.objects.create(
            kpi_name = kpi_name,
            process = process,
            created_by = user
        )
        return redirect('element_processes', pk=element.pk) #TODO: redirected to the created process page.

    return render(req, "new_process.html", {'element': element})

