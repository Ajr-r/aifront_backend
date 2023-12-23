from django.urls import path,include
from .views import test
from .views import t_to_t
urlpatterns = [
    path('test', test),
    path('ttot', t_to_t),
]