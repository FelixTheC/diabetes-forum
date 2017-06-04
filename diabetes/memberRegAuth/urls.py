from django.conf.urls import url
from .views import RegFormView

app_name = 'register'
urlpatterns = [
    url(r'^$',  RegFormView.as_view(), name='register')
]
