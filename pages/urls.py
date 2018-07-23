from django.urls import path
from django.urls import re_path as url
from .views import *
from accounts.views import signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', dashboard, name='home'),
    path('signup/', signup, name='signup'),
    url(r'^settings/password/$',
        auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^(?P<username>[\w\d.@+-]+)/?$', dashboard, name='home_page'),
    url(r'^(?P<username>[\w\d.@+-]+)/(?P<directory>[\w\d\s.@+-]+)/?$', navigate_directory, name='navigate_directory'),
    url(r'^(?P<username>[\w\d.@+-]+)/tag/(?P<tagname>[\w\d\s.@+-]+)/?$', navigate_directory, name='navigate_tag'),
    path('<username>/api/request', api_points, name='api_points'),
    path('<username>/<str:directory>/rename', rename_operation, name='rename_operation'),
    path('<username>/<str:directory>/remove', remove_operation, name='remove_operation'),
    path('<username>/<str:directory>/<int:url_id>/archieve', perform_link_operation, name='archieve_request'),
    path('<username>/<str:directory>/<int:url_id>/remove', perform_link_operation, name='remove_operation_link'),
    path('<username>/<str:directory>/<int:url_id>/read', perform_link_operation, name='read_link'),
    path('<username>/<str:directory>/<int:url_id>/edit-bookmark', perform_link_operation, name='edit_bookmark'),
    path('<username>/<str:directory>/<int:url_id>/move-bookmark', perform_link_operation, name='move_bookmark'),
    path('<username>/<str:directory>/<int:url_id>/move-bookmark-multiple', perform_link_operation, name='move_bookmark_multiple')
    
]

#url(r'^.*$', default_dest, name='catch_all')