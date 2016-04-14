from django.shortcuts import render
from django.http import HttpResponse



from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from polls.models import Meter
from polls.serializers import MeterSerializer



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def meter_list(request):
    print("meter list");
    if request.method == 'GET':
        meter = Meter.objects.all()
        serializer = MeterSerializer(meter, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def meter_detail(request, pk):
    print("meter detail" + pk);
    meter = Meter.objects.get(pk=pk)
    serializer = MeterSerializer(meter)
    return JSONResponse(serializer.data)







# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

