import logging, pdb
from rest_framework import serializers
from datetime import datetime

from jobs.models import Job

from django.contrib.auth.models import User, Group


try:
    from collections import OrderedDict
# python 2.6
except ImportError:
    from ordereddict import OrderedDict

# Get an instance of a logger
logger = logging.getLogger(__name__)

"""
class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    
    
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    

class UserGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    groups = GroupSerializer(many=True)
"""  

class JobSerializer(serializers.Serializer):
    """ Simple serializer to provide a subset of Route fields"""
    
    class Meta:
        model = Job
        fields = ('id','name','description','created','format','status', 'user')
        
    def create(self, validated_data):
        logger.debug(validated_data)
        request = self.context['request']
        id = request.user.id
        user = User.objects.get(id=id)
        return Job.objects.create(user=user, **validated_data)
    

