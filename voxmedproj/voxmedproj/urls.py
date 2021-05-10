from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from voxmed import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^voxmed/', include('voxmed.urls')),
    # url(r'^$', views.index, name='index'),
    url(r'^registermember',views.registerMember,  name='registerMember'),
    url(r'^login',views.login,  name='login'),
    url(r'^forgotpassword', views.forgotpassword, name='forgotpassword'),
    url(r'^resetpassword/$', views.resetpassword, name='resetpassword'),
    url(r'^rstpwd', views.rstpwd, name='rstpwd'),
    url(r'^postreport', views.postreport, name='postreport'),
    url(r'^getallusers', views.getallusers, name='getallusers'),
    url(r'^getreports', views.getallreports, name='getallreports'),
    url(r'^getmember', views.getmember, name='getmember'),
    url(r'^updatereport', views.updatereport, name='updatereport'),
    url(r'^updatemember', views.updatemember, name='updatemember'),
    url(r'^getreportpictures', views.getreportpictures, name='getreportpictures'),
    url(r'^pictures', views.pictures, name='pictures'),

    url(r'^newpic', views.newpic, name='newpic'),
    url(r'^getReportFields', views.getReportFields, name='getReportFields'),

    url(r'^saveKeywords', views.saveKeywords, name='saveKeywords'),
    url(r'^getKeywords', views.getKeywords, name='getKeywords'),

    url(r'^getAllKeywords', views.getAllKeywords, name='getAllKeywords'),

    url(r'^getTemplates', views.getTemplates, name='getTemplates'),
    url(r'^deleteTemplate', views.deleteTemplate, name='deleteTemplate'),

    url(r'^mailReport', views.mailReport, name='mailReport'),

    url(r'^getpatient', views.getpatient, name='getpatient'),




    ######### Admin ################################################################

    url(r'^$', views.loginpage, name='loginpage'),
    url(r'^signinprocess',views.adminloginprocess,  name='adminloginprocess'),
    url(r'^logout',views.logout,  name='logout'),
    url(r'^home',views.home,  name='home'),
    url(r'^doctors',views.doctors,  name='doctors'),
    url(r'^employees',views.employees,  name='employees'),
    url(r'^patients',views.patients,  name='patients'),
    url(r'^reports',views.reports,  name='reports'),
    url(r'^adminsetting',views.adminsetting,  name='adminsetting'),
    url(r'^addadminaccount',views.addadminaccount,  name='addadminaccount'),
    url(r'^delaccount/(?P<account_id>[0-9]+)',views.deleteAccount,  name='deleteAccount'),
    url(r'^removemember',views.removemember,  name='removemember'),
    url(r'^manage',views.manage,  name='manage'),
    url(r'^reportupdate',views.reportupdate,  name='reportupdate'),
    url(r'^newreport',views.newreport,  name='newreport'),
    url(r'^tempdelete',views.tempdelete,  name='tempdelete'),
    url(r'^keyworddelete',views.keyworddelete,  name='keyworddelete'),
    url(r'^newTemplateAdd',views.newTemplateAdd,  name='newTemplateAdd'),
    url(r'^newKeywordAdd',views.newKeywordAdd,  name='newKeywordAdd'),
    url(r'^tempchoose',views.tempchoose,  name='tempchoose'),
    url(r'^reportpost',views.reportpost,  name='reportpost'),
    url(r'^reportdelete',views.reportdelete,  name='reportdelete'),
    url(r'^docpatients',views.docpatients,  name='docpatients'),
    url(r'^newpatient',views.newpatient,  name='newpatient'),

    url(r'^patientremove',views.patientremove,  name='patientremove'),
    url(r'^export_xlsx',views.export_xlsx,  name='export_xlsx'),


    url(r'^test',views.test,  name='test'),

]


urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




























