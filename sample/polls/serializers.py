from rest_framework import serializers
from polls.models import Meter

class MeterSerializer(serializers.ModelSerializer):
    meters = serializers.StringRelatedField(many=True)
    class Meta:
        model = Meter
        fields = ('id', 'active', 'area', 'latitude', 'longitude', 'meter_id', 'street_address', 'meters')

