from django.shortcuts import render
from .models import regUser
from .forms import regForm
from django.views.generic import FormView

# Create your views here.
class RegFormView(FormView):
    form_class = regForm
    template_name = 'form.html'

    def form_valid(self, form, **kwargs):
        return super(RegFormView, **kwargs).form_valid(self)
