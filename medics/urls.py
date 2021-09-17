from django.contrib import admin
from django.urls import include, path
admin.site.site_header = 'Medics'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
