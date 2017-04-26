# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from isnull_filter.urls import urlpatterns as isnull_filter_urls

urlpatterns = [
    url(r'^', include(isnull_filter_urls, namespace='isnull_filter')),
]
