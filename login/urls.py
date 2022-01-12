from django.urls import path
from django.conf.urls import url
from . import views
from . views import CreateNewprojView
from . views import fullview
from . views import delete_proj
from . views import grades
from . views import editproj
from . views import sprojview
from . views import *
from . views import Student_profile

urlpatterns = [
    path('', views.index, name='index'),
    path('registerstud/', views.registerstud, name='registerstud'),
    path('registertr/', views.registertr, name='registertr'),
    path('tlogin/', views.tlogin, name='tlogin'),

    path('slogin/', views.slogin, name='slogin'),
    path('sdash/', views.sdash, name='sdash'),
    #path('newproject/',views.newproject, name='newproject'),
    #path('grades/',views.grades, name='grades'),
    path('logout/', views.logout, name='logout'),
    path('post/', CreateNewprojView.as_view(), name='add_post'),
    path('editproj/', views.editproj, name='editproj'),
    #path('sdash/', CreateNewprojView.as_view(), name='add_post'),
    #path('post/CreateNewprojView/', views.CreateNewprojView, name='CreateNewprojView'),
    #path('post/', views.enter_proj, name='post'),
    path('miniprojview/', views.miniprojview, name='miniprojview'),
    path('sprojview/', views.sprojview, name='sprojview'),
    path('Tinfo/', views.Tinfo, name='Tinfo'),
    #url(r'^sprojview/(?P<pk>\d+)$',views.sprojview, name='sprojview'),
    path(r'^sfullview/(?P<pk>\d+)$', views.sfullview, name='sfullview'),
    #path('grades/miniprojview/',views.miniprojview, name='miniprojview'),
    url(r'^fullview/(?P<pk>\d+)$', views.fullview, name='fullview'),
    url(r'^editproj/(?P<pk>\d+)$', views.editproj, name='editproj'),
    url(r'^sprojview/(?P<pk>\d+)$', views.delete_proj, name='delete_proj'),
    url(r'^grades/(?P<pk>\d+)$', views.grades, name='grades'),
    #path('fullview/',views.fullview, name='fullview')
    url(r'^profile/$',
        views.Student_profile, name='Student_profile'),
    path('registerstud/student_profile2',
         views.student_profile2, name='student_profile2'),
    url(r'^edit_profile/(?P<username>\w+)$',
        views.edit_profile, name='edit_profile'),

]
