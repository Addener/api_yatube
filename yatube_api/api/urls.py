from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewList
from api.views import FollowViewList
from api.views import GroupViewList
from api.views import PostViewSet


app_name = 'api'

router_v1 = SimpleRouter()

router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewList)
router_v1.register('follow', FollowViewList, basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewList, basename='comment')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
