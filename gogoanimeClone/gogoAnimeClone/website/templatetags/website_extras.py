from django import template
import re


register = template.Library()


@register.simple_tag
def define(val=None):
    return val


@register.simple_tag
def urlbuilder(string1, string2):
    bad_characters = ":;,.!?"
    string1 = string1.lower() + "-" + string2.lower()
    string1 = string1.replace(" ", "-")
    result = re.sub(rf'[{bad_characters}]', '', string1)
    return result


@register.simple_tag
def genrebuilder(*args):
    bad_characters = ":;,.!?"
    result = ""
    for item in args:
        result = item.lower() + result
    string1 = result.replace(" ", "-")
    result = re.sub(rf'[{bad_characters}]', '', string1)
    return result
