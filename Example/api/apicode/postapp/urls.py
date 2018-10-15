from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostViewSet,
                base_name='post')
urlpatterns = [
    url(r'^', include(router.urls)),
]
