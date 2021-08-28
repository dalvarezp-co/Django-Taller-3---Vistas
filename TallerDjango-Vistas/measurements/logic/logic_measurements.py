from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_by_pk(m_pk):
    measurement_pk = Measurement.objects.filter(pk=m_pk)
    return measurement_pk

def del_measurement_by_pk(m_pk):
    measurement_pk = Measurement.objects.filter(pk=m_pk)
    measurement_pk.delete()

def upd_measurement_by_pk(m_pk, pVal):
    measurement_pk = Measurement.objects.filter(pk=m_pk)
    measurement_pk.update(value=pVal)