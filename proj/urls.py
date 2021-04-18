from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from proj.views import (AllAccount, AllDataLog, AllStatusLog, AllMaintenance, AccountLogin, LatestReadings,LastDataLog, LatestStatus, LastStatusLog)

urlpatterns = [
    path('user/',AllAccount.as_view(),name="register_user"),
    path('data/',AllDataLog.as_view(),name="data"),
    path('status/',AllStatusLog.as_view(),name="status"),
    path('maintenance/',AllMaintenance.as_view(),name="maintenance"),
    path('data/<int:chamber_id>/',LastDataLog.as_view(),name="last_data"),
    path('user/login/',AccountLogin.as_view(),name="login_user"),
    path('data/last/<int:chamber_id>/',LatestReadings.as_view(),name="latest_15_readings"),
    path('status/last/',LastStatusLog.as_view(),name="last_status"),
    path('status/latest/',LatestStatus.as_view(),name="latest_15_status_readings"),
]

