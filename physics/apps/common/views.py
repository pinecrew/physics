from django.views.generic import View, TemplateView
from django.shortcuts import render

class ContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ContextMixin, self).get_context_data(**kwargs)
        return context


class Index(ContextMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({'active': 'index'})
        return context

    def get(self, request, *args, **kwargs):
        return super(Index, self).get(request, *args, **kwargs)

index = Index.as_view()
