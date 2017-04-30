from django import template
from firepit.models import HomeSolution

register = template.Library()

@register.assignment_tag
def request_quote():
	return HomeSolution.objects.get(order_number=1)

@register.assignment_tag
def decorate_space():
	return HomeSolution.objects.get(order_number=2)


@register.assignment_tag
def power_solution():
	return HomeSolution.objects.get(order_number=3)
