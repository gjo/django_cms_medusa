# -*- coding: utf-8 -*-

from cms.models import Page
from django.contrib.sites.models import Site
from django_medusa.renderers import StaticSiteRenderer


class CmsRenderer(StaticSiteRenderer):
    def get_paths(self):
        urls = []
        site = Site.objects.get_current()
        for page in Page.objects.public().published(site):
            for title in page.title_set.all():
                if title.path:
                    urls.append('/{}/{}/'.format(title.language, title.path))
                else:
                    urls.append('/{}/'.format(title.language))
        return frozenset(urls)


renderers = (CmsRenderer,)
