from django.conf.urls import include,url
from rest_framework import routers
from testauth.soustest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


#from django.conf.urls import include,url
#from rest_framework import routers
#from testauth.soustest import views
#from rest_framework.authtoken.views import obtain_auth_token

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)

#urlpatterns = {
    #url(r'^', include(router.urls)),
    #url(r'^auth',obtain_auth_token),
#}