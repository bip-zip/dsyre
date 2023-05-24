
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('syrapp.urls')),
    path('attendance', include('attendance.urls')),
    path('progress/', include('progressmeter.urls')),
    path('finance/', include('finance.urls')),
       path('tinymce/', include('tinymce.urls')),
]


from django.contrib import admin

admin.site.site_header = 'dSYRE Admin'                    # default: "Django Administration"
admin.site.index_title = 'dSYRE'                 # default: "Site administration"
admin.site.site_title = 'dSYRE adminsitration' # default: "Django site admin"

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)