from django.contrib import admin
from .models import About
# Register your models here.




class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
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
admin.site.register(About,AboutAdmin)




#DAY01-Settings aciqlamasi ucun ,acidigim Settigng_izahat.py baxin zehmet olmasa