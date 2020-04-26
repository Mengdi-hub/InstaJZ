from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HelloWorld(TemplateView): #HelloWorld is a TemplateView, now it has all attribute and methods of TemplateView
    template_name = 'test.html'