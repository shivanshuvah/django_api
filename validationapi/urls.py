  
from django.conf.urls import url
import views


urlpatterns=[
    url(r'finitevalues/',views.finitevalues),
    url(r'numericvalues/',views.numericvalues)
]