# Django
from django.views.generic  import TemplateView

###############
#### INDEX ####
###############

class IndexView(TemplateView):

    template_name = "core/index.html"