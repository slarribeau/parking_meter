
from rest_framework import serializers
from polls.models import Meter


"""
class MeterSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    active = serializers.CharField(max_length=48);
    area = serializers.CharField(max_length=48);
    latitude = serializers.FloatField();
    longitude = serializers.FloatField();
    meter_id = serializers.CharField(max_length=48);
    street_address = serializers.CharField(max_length=48);

    def create(self, validated_data):
        return Model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.active = validated_data.get('active', instance.active)
        instance.area = validated_data.get('area', instance.area)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.meter_id = validated_data.get('meter_id', instance.meter_id)
        instance.street_address = validated_data.get('street_address', instance.street_address)
        instance.save()
        return instance

"""
class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = ('id', 'active', 'area', 'latitude', 'longitude', 'meter_id', 'street_address')

