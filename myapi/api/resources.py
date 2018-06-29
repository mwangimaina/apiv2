from tastypie.resources import ModelResource
from .models import *
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()


class Form1Resource(ModelResource):
    class Meta:
        queryset = DataForm1.objects.all()
        resource_name = 'sitevisit'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()