from .logic.logic_measurements import get_all_measurements, get_measurement_by_pk, del_measurement_by_pk, upd_measurement_by_pk
from django.http import HttpResponse
from django.core import serializers
from .models import Measurement

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement_pk(request, m_pk):
    measurement = get_measurement_by_pk(m_pk)
    measurement_object = serializers.serialize('json', measurement)
    return HttpResponse(measurement_object, content_type='application/json')

def del_measurement_pk(request, m_pk):
    measurement_pk = get_measurement_pk(request, m_pk)
    measurement = del_measurement_by_pk(m_pk)
    return HttpResponse(measurement_pk, content_type='application/json')

def upd_measurement_pk(request, m_pk, pVal):
    measurement = upd_measurement_by_pk(m_pk, pVal)
    measurement_pk = get_measurement_pk(request, m_pk)
    return HttpResponse(measurement_pk, content_type='application/json')

# Create your views here.
