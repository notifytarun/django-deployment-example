from django.urls import path
from rel_app import views


basic_app = 'rel_app'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
    path('base/',views.base)
]



