from django.shortcuts import render, get_object_or_404

from sms_app.models import Element
from django.http import HttpResponse, Http404

# Create your views here.

def home(req):
    elements = Element.objects.all()
    return render(req, "home.html", {"elements":elements})

def element_processes(req, pk):
    element = get_object_or_404(Element, pk=pk)
    return render(req, 'process.html', {'element':element})


