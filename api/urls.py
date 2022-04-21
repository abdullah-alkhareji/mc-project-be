from django import urls
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from semester import views as semesterViews
from project import views as projectViews
from team import views as teamViews
from criteria import views as criteriaViews


router = SimpleRouter()
router.register('semester', semesterViews.SemesterViewSet)
router.register('project', projectViews.ProjectViewSet)
router.register('team', teamViews.TeamViewSet)
router.register('criteria', criteriaViews.CriteriaViewSet)
# print(router.urls)

urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('',include(router.urls))
]