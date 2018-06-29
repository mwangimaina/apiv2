from django.conf.urls import url, include
from tastypie.api import Api
from .resources import Form1Resource

v1_api = Api(api_name='v1')
v1_api.register(Form1Resource())


urlpatterns = [url(r'^api/', include(v1_api.urls))]