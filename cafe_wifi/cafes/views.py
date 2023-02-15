from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from .models import Cafe
from .forms import CafeForm
from random import choice
from django.forms.models import model_to_dict
import json


# Create your views here.
def home(request):
    return render(request, 'index.html')


class CafeCreateView(CreateView):
    template_name = 'add.html'
    form_class = CafeForm


class CafeListView(ListView):
    template_name = 'cafes.html'
    queryset = Cafe.objects.all()


# API
def get_all_cafe(request):
    data = list(Cafe.objects.all().values())
    return JsonResponse(data, safe=False)


def get_random_cafe(request):
    all_cafes = Cafe.objects.all()
    random_cafe = choice(all_cafes)
    dict_obj = model_to_dict(random_cafe)
    serialized = json.dumps(dict_obj, default=str)
    return HttpResponse(serialized)
