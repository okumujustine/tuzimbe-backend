
from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.get_all_workers, name="all_workers"),
    path("add/", views.add_worker, name="add_worker"),
    path("daily_works/", views.get_daily_works, name="get_daily_works"),
    path("add_daily_worker/", views.add_daily_worker, name="add_daily_worker"),
    path("filter/", views.WorkerFilter.as_view(), name="filter_workers"),
    path("attendance/", views.DailyAttendance.as_view(), name="attendance"),
    path("set_departure_time/", views.set_departure_time, name="set_departure_time")
]
