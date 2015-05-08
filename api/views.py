import logging, os, shutil, pdb
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.db.models import FileField
from rest_framework import views
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import status
from rest_framework import renderers
from rest_framework import generics
from rest_framework import filters
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.response import Response

from jobs.models import Job

from rest_framework.decorators import api_view, permission_classes
from jobs.models import Job
from serializers import (JobSerializer)


# Get an instance of a logger
logger = logging.getLogger(__name__)

renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        


class JobViewSet(viewsets.ModelViewSet):
    """
    Job API Endpoint
    """
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (FormParser, MultiPartParser)
    
    def get_queryset(self):
        return Job.objects.all()
    
    def create(self, request, *args, **kwargs):
        data = {}
        data['name'] = request.DATA['name']
        serializer = JobSerializer(data=data, context={'request': request})
        job = None
        if (serializer.is_valid()):
            job = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.debug(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        

    
    


    
