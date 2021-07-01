<!-------------------------------------------------Model-------------------------------------------------------->

                    <!-- Media -->
Site/url:
from django.conf import settings
from django.conf.urls.static import static

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Site/settings:
STATIC_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



Filds:
created_at = models.Datefield(auto_now_add=True)
updated_at = models.Datefield(auto_now=True)



Class Meta:
    ordering = ('title', '-created_at')