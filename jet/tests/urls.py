from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()


try:
    from django.urls import path

    urlpatterns = [
        path("jet/", include("jet.urls", "jet")),
        path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
        path("admin/doc/", include("django.contrib.admindocs.urls")),
        path("admin/", admin.site.urls),
    ]
except ImportError:  # Django < 2.0
    urlpatterns = [
        url(r"^jet/", include("jet.urls", "jet")),
        url(r"^jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
        url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
        url(r"^admin/", include(admin.site.urls)),
    ]
