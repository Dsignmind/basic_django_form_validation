from django.urls import re_path, path
from basicapp import views

urlpatterns = [
    path('formpage/', views.form_name_view, name='form_name'),
]