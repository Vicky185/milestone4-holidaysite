from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_packages, name='packages'),
    path('<package_id>', views.one_package_detail, name='one_package_detail'),
]
