from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'interviews/other/about.html'
