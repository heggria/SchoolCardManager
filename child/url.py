from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'show_collegeInfo$', views.show_collegeInfo),
    url(r'show_studentInfo$', views.show_studentInfo),
    url(r'get_studentInfo$', views.get_studentInfo),
    url(r'getExpenditureInfo$', views.getExpenditureInfo),
    url(r'getIncomeInfo$', views.getIncomeInfo),
    url(r'pay$', views.pay),
    url(r'login$', views.login),
    url(r'recharge$', views.recharge),
    url(r'changePassword$', views.changePassword),
    url(r'reportLoss$', views.reportLoss),
    url(r'cancelReportLoss$', views.cancelReportLoss),
    url(r'getReportLoss$', views.getReportLoss),
    url(r'registered$', views.registered),
    url(r'RPW$', views.RPW),
    ]