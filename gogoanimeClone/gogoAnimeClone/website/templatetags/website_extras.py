from django import template
import re


register = template.Library()


@register.simple_tag
def define(val=None):
    return val


@register.simple_tag
def episodebuilder(string1, string2):
    bad_characters = ":;,.!?"
    string1 = string1.lower() + "-" + string2.lower()
    string1 = string1.replace(" ", "-")
    result = re.sub(rf'[{bad_characters}]', '', string1)
    return result


@register.simple_tag
def namebuilder(*args):
    bad_characters = ":;,.!?"
    result = ""
    for item in args:
        result = item.lower() + result
    string1 = result.replace(" ", "-")
    result = re.sub(rf'[{bad_characters}]', '', string1)
    return result


@register.simple_tag
def replace(string1):
    string1 = string1.replace(" ", ": ")
    return string1


@register.simple_tag
def season_tag(season, year):
    result = f"{str(season.lower())}-{str(year)}-anime"
    return result
