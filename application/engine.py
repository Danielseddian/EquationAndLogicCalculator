from urllib import request
from django.forms import forms

from .calculator import rand_colors, calc_equation_sqrt


def calc_sqrt(form: forms):
    no_result = "Похоже, у этого уравнения нет решения."
    one_result = "Результат: {}"
    two_results = "Результат: {} и {}"
    results = calc_equation_sqrt(float(form.data["a_var"]), float(form.data["b_var"]), float(form.data["c_var"]))
    if len(results) == 2:
        return two_results.format(*map(str, results))
    elif result := results[0]:
        return one_result.format(str(result))
    return no_result


def guess_color(req: request, form: forms):
    if (user := req.user).is_authenticated:
        items = user.colors.values_list("number", "color")
        if item := items.filter(number=form.data["number"]):
            return item.values_list("color")[0][0]
        else:
            color = rand_colors(
                items.filter(color="b").count(), items.filter(color="g").count(), items.filter(color="r").count()
            )
            new_item = form.save(commit=False)
            new_item.user, new_item.color = user, color
            new_item.save()
            return color
    else:
        return rand_colors()
