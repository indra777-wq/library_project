from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    BookListApiView,
    BookDetailApiView,
    BookUpdateApiView,
    BookDeleteApiView,
    BookCreateApiView,
    BookListCreateApiView,
    BookUpdateDeleteApiView,
    BookViewSet,
    ComicsUpdateApiView,
    ComicsListApiView
)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
        # path('books/', BookListApiView.as_view()),
        # path('booklistcreate/', BookListCreateApiView.as_view()),
        # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),
        # path('books/create', BookCreateApiView.as_view()),
        # path('books/<int:pk>/', BookDetailApiView.as_view()),
        # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
        # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
        # path('comics/<int:pk>/update/', ComicsUpdateApiView.as_view()),
        # path('comics/', ComicsListApiView.as_view()),
]
urlpatterns = urlpatterns + router.urls
