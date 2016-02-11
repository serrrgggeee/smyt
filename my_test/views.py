# -*- coding: utf-8 -*-

from datetime import date

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.dates import ArchiveIndexView
from django.shortcuts import render

from .models import Test, Count

class TestItemDetailView(DetailView):
    model = Test
    context_object_name = 'test'
    def get_queryset(self):
        request = self.request
        user = str(request.user)
        path = str(request.path)
        try:
            q = Count(title=user, name=path)
            q.save()
            return super(TestItemDetailView, self).get_queryset()
        except Exception:
            return super(TestItemDetailView, self).get_queryset()


    def render_to_response(self, context, **response_kwargs):
        #

        context['count'] = Count.objects.all()
        return super(TestItemDetailView, self).render_to_response(context, **response_kwargs)
