from django.forms import widgets
from rest_framework import serializers
from urlexp.models import urlInfo

class infoSerializer(serializers.ModelSerializer):
	class Meta:
		model = urlInfo
		fields = ('short', 'expanded', 'status', 'title', 'waybackUrl', 'waybackTime', 'screen')

	
