<!-- -----------------------------------------------Model------------------------------------------------------

                        <!-- Media -->
Site/urls:
from django.conf import settings
from django.conf.urls.static import static

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Site/settings:
STATIC_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



Filds:
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)



Class Meta:
    ordering = ('title', '-created_at')



Relations:
A)1 yazicinin coxlu kitabi olar biler(one to many)

ForeignKey cox terefe verilir ,yeni hansi hansindan aslidir. Kitab yazicidan asili deyil.
ForeignKey asli terefde olur.
ForeignKey verende foreignKey vereceymiz teref cox teref olmalidir.



B)coxlu Receipe  1 Category(one to many):
a Category-de 10 dene Receipe ola biler.

COX TEREF HARDADIRSA RELATIONS ORA VERILIR. -->