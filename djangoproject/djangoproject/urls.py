from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from mainapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'user-data', views.UserDataViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogout),
]

urlpatterns += router.urls