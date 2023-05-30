from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user/<int:id>', views.user),
    path('user/files/<int:id>', views.user_files),
    path('user/id/check/<int:id>', views.user_id_check),
    path('user/otp/verify/<str:email>', views.user_verify_email),
    path('jobs', views.jobs),
    path('companies', views.companies),
    path('job/<int:id>', views.job),
    path('company/<int:id>', views.company),
    path('user/login', views.user_login),
    path('job/apply', views.job_apply),
    path('job/check', views.job_check),
    path('search/<str:query>', views.search),
    path('user/notifications/<int:id>', views.notifications),
    path('job/count/<int:id>', views.job_count),
]
