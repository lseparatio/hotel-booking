from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static, re_path
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path(_('admin/'), admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('rosetta/', include('rosetta.urls')),
    path('', include('home.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
