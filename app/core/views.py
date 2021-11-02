# Django
from django.views.generic  import View, TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

# Models
from .models import *

###############
#### INDEX ####
###############

class IndexView(TemplateView):

    template_name = "core/index.html"

###################
#### Biography ####
###################

class BiographyView(TemplateView):

    template_name = "core/biography.html"

#################
#### Contact ####
#################

class ContactCreateView(CreateView):

    template_name = "core/biography.html"
    model = Contato

###################
#### Dark Mode ####
###################

class DarkModeView(View):

    def get(self, request, *args, **kwargs):

        raise PermissionDenied()

    def post(self, request, *args, **kwargs):

        current_dark_mode_state = request.session.get('dark_mode')

        if current_dark_mode_state:
            request.session['dark_mode'] = False
        else:
            request.session['dark_mode'] = True
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))