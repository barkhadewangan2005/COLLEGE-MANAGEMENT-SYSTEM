"""
API ViewSets for REST API
"""
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    CustomUser, Staffs, Students, Courses, Subjects,
    Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff,
    StudentResult, Timetable, Announcement, Notification, SessionYearModel
)
from .serializers import (
    UserSerializer, StaffSerializer, StudentSerializer,
    CourseSerializer, SubjectSerializer, AttendanceSerializer,
    AttendanceReportSerializer, LeaveReportStudentSerializer,
    LeaveReportStaffSerializer, StudentResultSerializer,
    TimetableSerializer, AnnouncementSerializer, NotificationSerializer,
    SessionYearSerializer
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing users
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['date_joined', 'username']
    ordering = ['-date_joined']


class SessionYearViewSet(viewsets.ModelViewSet):
    """
    API endpoint for session years
    """
    queryset = SessionYearModel.objects.all()
    serializer_class = SessionYearSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['-session_start_year']


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for courses
    """
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['course_name']
    ordering_fields = ['course_name', 'created_at']
    ordering = ['course_name']
    
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        """Get all students in this course"""
        course = self.get_object()
        students = Students.objects.filter(course_id=course)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        """Get all subjects in this course"""
        course = self.get_object()
        subjects = Subjects.objects.filter(course_id=course)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for subjects
    """
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['course_id', 'staff_id']
    search_fields = ['subject_name']
    ordering_fields = ['subject_name', 'created_at']
    ordering = ['subject_name']


class StaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint for staff
    """
    queryset = Staffs.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['admin__username', 'admin__email', 'admin__first_name', 'admin__last_name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        """Get all subjects taught by this staff"""
        staff = self.get_object()
        subjects = Subjects.objects.filter(staff_id=staff.admin)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for students
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['course_id', 'session_year_id', 'gender']
    search_fields = ['admin__username', 'admin__email', 'admin__first_name', 'admin__last_name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    @action(detail=True, methods=['get'])
    def attendance(self, request, pk=None):
        """Get attendance records for this student"""
        student = self.get_object()
        attendance = AttendanceReport.objects.filter(student_id=student)
        serializer = AttendanceReportSerializer(attendance, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def results(self, request, pk=None):
        """Get exam results for this student"""
        student = self.get_object()
        results = StudentResult.objects.filter(student_id=student)
        serializer = StudentResultSerializer(results, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def leaves(self, request, pk=None):
        """Get leave applications for this student"""
        student = self.get_object()
        leaves = LeaveReportStudent.objects.filter(student_id=student)
        serializer = LeaveReportStudentSerializer(leaves, many=True)
        return Response(serializer.data)


class AttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for attendance
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['subject_id', 'session_year_id', 'attendance_date']
    ordering_fields = ['attendance_date', 'created_at']
    ordering = ['-attendance_date']
    
    @action(detail=True, methods=['get'])
    def reports(self, request, pk=None):
        """Get individual attendance reports for this attendance"""
        attendance = self.get_object()
        reports = AttendanceReport.objects.filter(attendance_id=attendance)
        serializer = AttendanceReportSerializer(reports, many=True)
        return Response(serializer.data)


class AttendanceReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint for attendance reports
    """
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student_id', 'attendance_id', 'status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class LeaveReportStudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for student leave reports
    """
    queryset = LeaveReportStudent.objects.all()
    serializer_class = LeaveReportStudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student_id', 'leave_status']
    ordering_fields = ['created_at', 'leave_date']
    ordering = ['-created_at']
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve leave application"""
        leave = self.get_object()
        leave.leave_status = 1
        leave.save()
        serializer = self.get_serializer(leave)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Reject leave application"""
        leave = self.get_object()
        leave.leave_status = 2
        leave.save()
        serializer = self.get_serializer(leave)
        return Response(serializer.data)


class LeaveReportStaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint for staff leave reports
    """
    queryset = LeaveReportStaff.objects.all()
    serializer_class = LeaveReportStaffSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['staff_id', 'leave_status']
    ordering_fields = ['created_at', 'leave_date']
    ordering = ['-created_at']
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve leave application"""
        leave = self.get_object()
        leave.leave_status = 1
        leave.save()
        serializer = self.get_serializer(leave)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Reject leave application"""
        leave = self.get_object()
        leave.leave_status = 2
        leave.save()
        serializer = self.get_serializer(leave)
        return Response(serializer.data)


class StudentResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint for student results
    """
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student_id', 'subject_id']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class TimetableViewSet(viewsets.ModelViewSet):
    """
    API endpoint for timetable
    """
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course', 'session_year', 'day_of_week', 'subject']
    ordering_fields = ['day_of_week', 'start_time']
    ordering = ['day_of_week', 'start_time']


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    API endpoint for announcements
    """
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['target_audience', 'is_active']
    search_fields = ['title', 'message']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for notifications
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'notification_type', 'is_read']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    @action(detail=False, methods=['get'])
    def my_notifications(self, request):
        """Get notifications for current user"""
        notifications = Notification.objects.filter(user=request.user)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def unread_count(self, request):
        """Get unread notification count for current user"""
        count = Notification.objects.filter(user=request.user, is_read=False).count()
        return Response({'unread_count': count})
    
    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        """Mark notification as read"""
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def mark_all_read(self, request):
        """Mark all notifications as read for current user"""
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return Response({'message': 'All notifications marked as read'})
