from django.urls import path
from . import views

urlpatterns = [
    path('get_data', views.getData, name="get_data"),
    path('view-package/<slug>', views.view_package, name="view-package"),
    path('manage-site', views.manage_site, name="manage-site"),
    path('add-package', views.add_package, name="add-package"),
    path('add-course', views.add_course, name="add-course"),
    path('payment-success', views.payment_success, name="payment-success"),
]
