from django.views.generic.base import TemplateView


class IndexTemplate(TemplateView):
    template_name = 'index.html'
