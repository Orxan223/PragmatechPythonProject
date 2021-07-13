from django import template
register = template.Library()
    
from ..models import Skill
  
@register.simple_tag
def any_function():
      return Skill.objects.count()