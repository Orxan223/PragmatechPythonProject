from django.contrib import admin
from .models import About  , Choose, Blog  ,Skill,Category  , News,Contact,Category,Profession,Pese
# Register your models here.





# ---------------------------------------      About     ---------------------------------- 

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(About,AboutAdmin)


# ---------------------------------------      Choose     ---------------------------------- 

class ChooseAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Choose,ChooseAdmin)





# # ---------------------------------------      Skill     ---------------------------------- 

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Skill,SkillAdmin)


admin.site.register(Category)




# ---------------------------------------      Blog     ---------------------------------- 

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Blog,BlogAdmin)




admin.site.register(Profession)

# ---------------------------------------      News     ---------------------------------- 

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(News,NewsAdmin)




admin.site.register(Pese)



# ---------------------------------------      Contact     ---------------------------------- 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Contact,ContactAdmin)
















