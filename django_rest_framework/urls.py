from django.conf.urls import url, include
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from quickstart.form import LoginForm
from django.contrib import admin

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'questions', views.QuestionViewSet)
# router.register(r'choices', views.ChoiceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls), name='home'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^question/$', views.question_list, name='question_list'),
    url(r'^question/create/$', views.question_create, name='add_question'),
    url(r'^question/update/(?P<pk>\d+)/$', views.question_update, name='question_update'),
    url(r'^question/(?P<pk>\d+)/delete/$', views.question_delete, name='question_delete'),
    url(r'^choice/$', views.choice_list, name='choice_list'),
    url(r'^choice/create/$', views.choice_create, name='choice_create'),
    url(r'^choice/update/(?P<pk>\d+)/$', views.choice_update, name='choice_update'),
    url(r'^choice/(?P<pk>\d+)/delete/$', views.choice_delete, name='choice_delete'),
    url(r'^login/$', auth_views.login, {'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)