from django.contrib import admin
from .models import News,Pese
# Register your models here.
# ---------------------------------------      News     ---------------------------------- 



@admin.register(News)
class NewsAdmin (admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ["title"],
    }

admin.site.register(Pese)
