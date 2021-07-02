from django.contrib import admin
from .models import Technology , About , Team , Choose , Case , Work , Blog , Category , News , Contact
# Register your models here.


# ---------------------------------------      Technology     ---------------------------------- 

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Technology,TechnologyAdmin)



# ---------------------------------------      About     ---------------------------------- 

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(About,AboutAdmin)


# ---------------------------------------      Choose     ---------------------------------- 

class ChooseAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Choose,ChooseAdmin)


# ---------------------------------------      Team     ---------------------------------- 

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Team,TeamAdmin)


# ---------------------------------------      Case     ---------------------------------- 

class CaseAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Case,CaseAdmin)





# ---------------------------------------      Work     ---------------------------------- 

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Work,WorkAdmin)



# ---------------------------------------      Blog     ---------------------------------- 

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Blog,BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category,CategoryAdmin)


# ---------------------------------------      News     ---------------------------------- 

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(News,NewsAdmin)



# ---------------------------------------      Contact     ---------------------------------- 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Contact,ContactAdmin)

















    #list_display = ('title',)
    # Menasindan da gorunduyu kimi listdeki elemetleri display etmek ucundur

    # fields = ('title',)
    # Yalniz qeyd edilen hisseni gosderir

    # exclude = ('title',)
    # Qeyd edilen yer xaric , digerlerini gosderir

    # list_filter = ('text',) 
    # Admin sehifesinde sag hissede gorduyumuz filterleme isini gormek ucundur. Meselen
    # qeyd etdiyimiz kimi text gore filterleme etsek ,veridiyimiz textlere esasen filterleme isleri aparilacaq

    # search_fields = ('title',)
    # Admin page-de serach ucun yer acilir, ve burada qeyd etdiyimiz title gore seacrh edib bize getirir