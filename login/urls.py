from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    # url(r'^$', login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.register, name='register'),
    url(r'^logout/$', views.logout_page, name ='logout'),
    url(r'^register/success/$', views.register_success, name ='register_success'),
]




# urlpatterns=[
#     url(r'^login/$', 'django.contrib.auth.views.login'),
#     url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
#     url(r'^home/$', 'login.views.home'),
# ]


# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]