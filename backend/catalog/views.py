from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main.html'
    
    def get(self, request):
        return render(request, self.template_name)