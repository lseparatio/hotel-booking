from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static, re_path
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path(_('admin/'), admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('favicon.ico', RedirectView.as_view(
    url = staticfiles_storage.url('img/favicon.ico'))),
    path('', include('home.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
