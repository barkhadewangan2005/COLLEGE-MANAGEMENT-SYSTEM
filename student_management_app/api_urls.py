"""
API URL Configuration
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import (
    UserViewSet, StaffViewSet, StudentViewSet,
    CourseViewSet, SubjectViewSet, AttendanceViewSet,
    AttendanceReportViewSet, LeaveReportStudentViewSet,
    LeaveReportStaffViewSet, StudentResultViewSet,
    TimetableViewSet, AnnouncementViewSet, NotificationViewSet,
    SessionYearViewSet
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'session-years', SessionYearViewSet, basename='session-year')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'attendance-reports', AttendanceReportViewSet, basename='attendance-report')
router.register(r'student-leaves', LeaveReportStudentViewSet, basename='student-leave')
router.register(r'staff-leaves', LeaveReportStaffViewSet, basename='staff-leave')
router.register(r'results', StudentResultViewSet, basename='result')
router.register(r'timetable', TimetableViewSet, basename='timetable')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'notifications', NotificationViewSet, basename='notification')

app_name = 'api'

urlpatterns = [
    # Authentication
    path('auth/login/', obtain_auth_token, name='api-login'),
    
    # ViewSet routes
    path('', include(router.urls)),
]
