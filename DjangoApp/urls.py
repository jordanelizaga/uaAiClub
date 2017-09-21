"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url
# from app.forms import BootstrapAuthenticationForm
# from app.views import *
# from app.models import *
# from django.contrib.auth.views import *


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
     
#     url(r'^$', home, name='home'),
#     url(r'^contact$', contact, name='contact'),
#     url(r'^about', about, name='about'),
#    url(r'^login/$', login, {
#             'template_name': 'app/login.html',
#             'authentication_form': BootstrapAuthenticationForm,
#             'extra_context':
#             {
#                 'title':'Log in',
#                 'year':datetime.now().year,
#             }
#         },
#         name='login'),
#        url(r'^logout$', logout, {  'next_page': '/'  },        name='logout')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
]

# Use include() to add URLS from the catalog application 
from django.conf.urls import include

urlpatterns += [
    url(r'^home/', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^resources/', include('resources.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/home/', permanent=True)),
]


# Use static() to add url mapping to serve static files during development (only) 
#### I KNOW IT ONLY SAYS DURING DEVELOPMENT BUT I DONT KNOW WHERE ELSE TO PUT STATIC FILES (CSS)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
