"""
Serializers for REST API
"""
from rest_framework import serializers
from .models import (
    CustomUser, Staffs, Students, Courses, Subjects,
    Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff,
    StudentResult, Timetable, Announcement, Notification,
    SessionYearModel
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class SessionYearSerializer(serializers.ModelSerializer):
    session_display = serializers.SerializerMethodField()
    
    class Meta:
        model = SessionYearModel
        fields = ['id', 'session_start_year', 'session_end_year', 'session_display']
    
    def get_session_display(self, obj):
        return f"{obj.session_start_year.year} - {obj.session_end_year.year}"


class CourseSerializer(serializers.ModelSerializer):
    student_count = serializers.SerializerMethodField()
    subject_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'created_at', 'student_count', 'subject_count']
        read_only_fields = ['id', 'created_at']
    
    def get_student_count(self, obj):
        return obj.students_set.count()
    
    def get_subject_count(self, obj):
        return obj.subjects_set.count()


class SubjectSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course_id.course_name', read_only=True)
    staff_name = serializers.CharField(source='staff_id.get_full_name', read_only=True)
    
    class Meta:
        model = Subjects
        fields = ['id', 'subject_name', 'course_id', 'course_name', 'staff_id', 'staff_name', 'created_at']
        read_only_fields = ['id', 'created_at']


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='admin', read_only=True)
    full_name = serializers.CharField(source='admin.get_full_name', read_only=True)
    email = serializers.CharField(source='admin.email', read_only=True)
    
    class Meta:
        model = Staffs
        fields = ['id', 'user', 'full_name', 'email', 'address', 'created_at']
        read_only_fields = ['id', 'created_at']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='admin', read_only=True)
    full_name = serializers.CharField(source='admin.get_full_name', read_only=True)
    email = serializers.CharField(source='admin.email', read_only=True)
    course_name = serializers.CharField(source='course_id.course_name', read_only=True)
    session_year = serializers.CharField(source='session_year_id.__str__', read_only=True)
    
    class Meta:
        model = Students
        fields = [
            'id', 'user', 'full_name', 'email', 'gender', 'profile_pic',
            'address', 'course_id', 'course_name', 'session_year_id',
            'session_year', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class AttendanceSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject_id.subject_name', read_only=True)
    session_year = serializers.CharField(source='session_year_id.__str__', read_only=True)
    present_count = serializers.SerializerMethodField()
    absent_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Attendance
        fields = [
            'id', 'subject_id', 'subject_name', 'attendance_date',
            'session_year_id', 'session_year', 'present_count',
            'absent_count', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_present_count(self, obj):
        return obj.attendancereport_set.filter(status=True).count()
    
    def get_absent_count(self, obj):
        return obj.attendancereport_set.filter(status=False).count()


class AttendanceReportSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student_id.admin.get_full_name', read_only=True)
    subject_name = serializers.CharField(source='attendance_id.subject_id.subject_name', read_only=True)
    attendance_date = serializers.DateField(source='attendance_id.attendance_date', read_only=True)
    
    class Meta:
        model = AttendanceReport
        fields = [
            'id', 'student_id', 'student_name', 'attendance_id',
            'subject_name', 'attendance_date', 'status', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class LeaveReportStudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student_id.admin.get_full_name', read_only=True)
    status_display = serializers.SerializerMethodField()
    
    class Meta:
        model = LeaveReportStudent
        fields = [
            'id', 'student_id', 'student_name', 'leave_date',
            'leave_message', 'leave_status', 'status_display', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_status_display(self, obj):
        status_map = {0: 'Pending', 1: 'Approved', 2: 'Rejected'}
        return status_map.get(obj.leave_status, 'Unknown')


class LeaveReportStaffSerializer(serializers.ModelSerializer):
    staff_name = serializers.CharField(source='staff_id.admin.get_full_name', read_only=True)
    status_display = serializers.SerializerMethodField()
    
    class Meta:
        model = LeaveReportStaff
        fields = [
            'id', 'staff_id', 'staff_name', 'leave_date',
            'leave_message', 'leave_status', 'status_display', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_status_display(self, obj):
        status_map = {0: 'Pending', 1: 'Approved', 2: 'Rejected'}
        return status_map.get(obj.leave_status, 'Unknown')


class StudentResultSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student_id.admin.get_full_name', read_only=True)
    subject_name = serializers.CharField(source='subject_id.subject_name', read_only=True)
    total_marks = serializers.SerializerMethodField()
    
    class Meta:
        model = StudentResult
        fields = [
            'id', 'student_id', 'student_name', 'subject_id', 'subject_name',
            'subject_exam_marks', 'subject_assignment_marks', 'total_marks', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_total_marks(self, obj):
        return obj.subject_exam_marks + obj.subject_assignment_marks


class TimetableSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject_name', read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)
    session_year = serializers.CharField(source='session_year.__str__', read_only=True)
    staff_name = serializers.CharField(source='subject.staff_id.get_full_name', read_only=True)
    
    class Meta:
        model = Timetable
        fields = [
            'id', 'subject', 'subject_name', 'course', 'course_name',
            'session_year', 'day_of_week', 'start_time', 'end_time',
            'room_number', 'staff_name', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = Announcement
        fields = [
            'id', 'title', 'message', 'target_audience',
            'created_by', 'created_by_name', 'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class NotificationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = Notification
        fields = [
            'id', 'user', 'user_name', 'title', 'message',
            'notification_type', 'is_read', 'link', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
