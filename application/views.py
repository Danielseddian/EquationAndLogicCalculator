from urllib import request
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from .forms import GuessColorForm, CreationForm, EquationForm
from .engine import guess_color, calc_sqrt


def index(req: request):
    equation_form = EquationForm(req.POST or None)
    result = calc_sqrt(equation_form) if equation_form.is_valid() else None
    color_form = GuessColorForm(req.POST or None)
    color = guess_color(req, color_form) if color_form.is_valid() else None
    return render(
        req, "index.html", {"color_form": color_form, "color": color, "equation_form": equation_form, "result": result}
    )


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("application:index")
    template_name = "registration/signup.html"
