from django.urls import path

from test_project.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)