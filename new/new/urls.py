"""
URL configuration for new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from testapi import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="mhapy",
        default_version='v1',
        description="API takes in user's free text, map it to a scaling system and store it to the database.",
        terms_of_service="https://www.example.com/policies/terms/",
        # contact=openapi.Contact(email="contact@example.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()

# router.register(r'assessments', views.UserInputViewSet, basename='assessments')
# router.register(r'result', views.ScoreViewSet, basename='result')
# router.register(r'questions', views.QuestionViewSet, basename='questions')


# router.register(r'assessments', views.AssessmentsViewSet, basename='assessments')

# Register the ScoreViewSet with the router.
# Similar to UserInputViewSet, this registers routes for handling scores,
# making them accessible under the 'scores' URL path.
# router.register(r'response', views.QuestionsViewSet, basename='questions')

router.register(r'questions', views.QuestionsViewSet, basename='questions')
# router.register(r'result', views.UserStatsViewSet, basename='result')

urlpatterns = [
  # Direct all URLs to the router
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('result/<int:user_id>/', views.UserStatsViewSet.as_view({'get': 'list'}), name='result'),
    path('response/<int:question_id>/', views.ResponsesViewSet.as_view({'get': 'list', 'post': 'create'}), name='response'),
]
