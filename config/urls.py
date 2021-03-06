from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView
from rest_framework.authtoken.views import obtain_auth_token


class HomeRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # redirects authenticated users to their brain list
        if self.request.user.is_authenticated:
            return reverse_lazy("studygroups:group_list_view")
        return reverse_lazy("start")


urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home"),
    path("start/", TemplateView.as_view(template_name="pages/home.html"), name="start"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path(
        "terms_and_conditions/",
        TemplateView.as_view(template_name="pages/terms_and_conditions.html"),
        name="terms_and_conditions",
    ),
    path(
        "privacy_policy/",
        TemplateView.as_view(template_name="pages/privacy_policy.html"),
        name="privacy_policy",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("memo.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    #
    # App url confs
    #
    path("group/", include("memo.studygroups.urls", namespace="studygroup")),
    path("card/", include("memo.flashcards.urls", namespace="flashcard")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
