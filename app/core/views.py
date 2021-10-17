# Django
from django.views.generic  import TemplateView, View
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

###############
#### INDEX ####
###############

class IndexView(TemplateView):

    template_name = "core/index.html"

###########################
#### Session Variables ####
###########################

class DarkModeView(View):

    def get(self, request, *args, **kwargs):

        raise PermissionDenied()

    def post(self, request, *args, **kwargs):

        try:

            dark_mode = bool(int(request.POST.get('dark-mode')))

            if dark_mode:
                request.session['dark_mode'] = True
            else:
                request.session['dark_mode'] = False
        
        except:

            pass
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))