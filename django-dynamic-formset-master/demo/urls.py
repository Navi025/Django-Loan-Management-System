import django
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^examples/', include('example.urls')),
]

if 'ajax_select' in settings.INSTALLED_APPS:
    # If django-ajax-selects is installed, include its URLs:
    urlpatterns += [
        url(r'^ajax-select/', include('ajax_select.urls'))
    ]

if settings.DEBUG:
    urlpatterns += [
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1],
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    ]
