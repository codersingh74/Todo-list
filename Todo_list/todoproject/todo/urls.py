# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)  # sirf 'tasks' likhna hai

# urlpatterns = [
#     path('', include(router.urls)),
# ]



from django.urls import path
from .views import index
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', index, name='home'),  # 🆕 Yeh line add karo
]

urlpatterns += router.urls
