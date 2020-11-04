import views
from django.urls import path


urlpatterns=[
    path('numericvalues/',views.NumericValues.as_view(), name='numericvalues-view'),
    path('finitevalues/', views.FiniteValues.as_view(), name='finitevalues-view')
]