from django.urls import path
# from .views import ListPosts, PostDetail
from rest_framework.routers import SimpleRouter

from .views import ListPosts, PostDetail
router = SimpleRouter()
router.register('', ListPosts,basename="post_view")

urlpatterns = router.urls+ [  
    path('edit/<uuid:pk>/', PostDetail.as_view())
]


# urlpatterns = [
#     path('Post/', ListPosts.as_view()),
#     path('Post/<uuid:pk>/', PostDetail.as_view())

# ]