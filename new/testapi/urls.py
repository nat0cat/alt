from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import * 

# Create a router object to handle URL routing for the API.
router = DefaultRouter()

router.register(r'assessments', AssessmentsViewSet, basename='assessments')

# Register the ScoreViewSet with the router.
# Similar to UserInputViewSet, this registers routes for handling scores,
# making them accessible under the 'scores' URL path.
router.register(r'result', UserStatsViewSet, basename='result')

router.register(r'questions/', QuestionsViewSet, basename='questions')


# The urlpatterns list is now defined by the router's urls,
# automating the creation of URL patterns for the registered viewsets.
urlpatterns = router.urls
