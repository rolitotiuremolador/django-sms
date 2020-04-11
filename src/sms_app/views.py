
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
    user =  User.objects.first() #TODO: get the currently loggedin user
    if req.method == 'POST':
        form = NewProcessForm(req.POST or None)
        if form.is_valid():
            process = form.save(commit=False)
            process.element = element
            process.created_by = user
            process.save()
            kpi = Kpi.objects.create(
                kpi_name = form.cleaned_data.get('kpi_name'),
                process=process,
                created_by = user
            )
            return redirect('element_processes', pk=element.pk) #TODO: redirected to the created process page.
    else:
        form = NewProcessForm()
    return render(req, "new_process.html", {'element': element, 'form': form})

