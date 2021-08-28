from measurements.logic.logic_measurements import del_measurement_by_pk, get_measurement_by_pk
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('id/<int:m_pk>/', views.get_measurement_pk, name='measurementByPk'),
    path('del/<int:m_pk>/', views.del_measurement_pk, name='delMeasurementByPk'),
    path('upd/<int:m_pk>/<int:pVal>/', views.upd_measurement_pk, name='updMeasurementValue')
]