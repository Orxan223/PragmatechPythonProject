# from django import template
# register = template.Library()
    
# from ..models import Skill
  
# @register.simple_tag
# def any_function():
#       return Skill.objects.count()

# 2si eyni vaxda islemediyine gore commente aldim. Bunu isletmek isdedikde mes:<p>{{x.text}}{% any_function  %}</p> 
# yazmagimiz kifayetdir.


from django import template
register = template.Library()

import datetime

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

