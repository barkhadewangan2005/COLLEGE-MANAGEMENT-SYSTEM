# API Documentation

**Version:** 2.0.0  
**Last Updated:** January 5, 2026

## College Management System REST API

### Base URL
```
http://localhost:8000/api/
```

### Authentication

The API uses Token Authentication. To authenticate:

1. **Login to get token:**
```bash
POST /api/auth/login/
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

2. **Use token in requests:**
```bash
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

---

## API Endpoints

### 1. Users
- **List Users:** `GET /api/users/`
- **Get User:** `GET /api/users/{id}/`
- **Search:** `?search=john`
- **Ordering:** `?ordering=-date_joined`

### 2. Session Years
- **List:** `GET /api/session-years/`
- **Create:** `POST /api/session-years/`
- **Update:** `PUT /api/session-years/{id}/`
- **Delete:** `DELETE /api/session-years/{id}/`

### 3. Courses
- **List Courses:** `GET /api/courses/`
- **Get Course:** `GET /api/courses/{id}/`
- **Create Course:** `POST /api/courses/`
- **Update Course:** `PUT /api/courses/{id}/`
- **Delete Course:** `DELETE /api/courses/{id}/`
- **Get Course Students:** `GET /api/courses/{id}/students/`
- **Get Course Subjects:** `GET /api/courses/{id}/subjects/`

### 4. Subjects
- **List Subjects:** `GET /api/subjects/`
- **Filter by Course:** `?course_id=1`
- **Filter by Staff:** `?staff_id=2`
- **Search:** `?search=mathematics`

### 5. Staff
- **List Staff:** `GET /api/staff/`
- **Get Staff:** `GET /api/staff/{id}/`
- **Get Staff Subjects:** `GET /api/staff/{id}/subjects/`
- **Create Staff:** `POST /api/staff/`
- **Update Staff:** `PUT /api/staff/{id}/`

### 6. Students
- **List Students:** `GET /api/students/`
- **Get Student:** `GET /api/students/{id}/`
- **Filter:** `?course_id=1&session_year_id=1&gender=Male`
- **Get Student Attendance:** `GET /api/students/{id}/attendance/`
- **Get Student Results:** `GET /api/students/{id}/results/`
- **Get Student Leaves:** `GET /api/students/{id}/leaves/`

### 7. Attendance
- **List Attendance:** `GET /api/attendance/`
- **Create Attendance:** `POST /api/attendance/`
- **Filter:** `?subject_id=1&attendance_date=2025-12-31`
- **Get Reports:** `GET /api/attendance/{id}/reports/`

### 8. Attendance Reports
- **List Reports:** `GET /api/attendance-reports/`
- **Filter:** `?student_id=1&status=true`
- **Create Report:** `POST /api/attendance-reports/`

### 9. Student Leave Reports
- **List Leaves:** `GET /api/student-leaves/`
- **Create Leave:** `POST /api/student-leaves/`
- **Approve Leave:** `POST /api/student-leaves/{id}/approve/`
- **Reject Leave:** `POST /api/student-leaves/{id}/reject/`
- **Filter by Status:** `?leave_status=0` (0=Pending, 1=Approved, 2=Rejected)

### 10. Staff Leave Reports
- **List Leaves:** `GET /api/staff-leaves/`
- **Create Leave:** `POST /api/staff-leaves/`
- **Approve Leave:** `POST /api/staff-leaves/{id}/approve/`
- **Reject Leave:** `POST /api/staff-leaves/{id}/reject/`

### 11. Student Results
- **List Results:** `GET /api/results/`
- **Create Result:** `POST /api/results/`
- **Filter:** `?student_id=1&subject_id=2`
- **Update Result:** `PUT /api/results/{id}/`

### 12. Timetable
- **List Timetable:** `GET /api/timetable/`
- **Create Entry:** `POST /api/timetable/`
- **Filter:** `?course=1&day_of_week=Monday`
- **Update Entry:** `PUT /api/timetable/{id}/`
- **Delete Entry:** `DELETE /api/timetable/{id}/`

### 13. Announcements
- **List Announcements:** `GET /api/announcements/`
- **Create Announcement:** `POST /api/announcements/`
- **Filter:** `?target_audience=students&is_active=true`
- **Update:** `PUT /api/announcements/{id}/`
- **Delete:** `DELETE /api/announcements/{id}/`

### 14. Notifications
- **List Notifications:** `GET /api/notifications/`
- **My Notifications:** `GET /api/notifications/my_notifications/`
- **Unread Count:** `GET /api/notifications/unread_count/`
- **Mark as Read:** `POST /api/notifications/{id}/mark_read/`
- **Mark All Read:** `POST /api/notifications/mark_all_read/`
- **Filter:** `?notification_type=attendance&is_read=false`

---

## Example Requests

### Create Course
```bash
curl -X POST http://localhost:8000/api/courses/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "course_name": "Computer Science"
  }'
```

### Create Student
```bash
curl -X POST http://localhost:8000/api/students/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "admin": 5,
    "gender": "Male",
    "address": "123 Main St",
    "course_id": 1,
    "session_year_id": 1
  }'
```

### Mark Attendance
```bash
curl -X POST http://localhost:8000/api/attendance/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "subject_id": 1,
    "attendance_date": "2025-12-31",
    "session_year_id": 1
  }'
```

### Create Attendance Reports
```bash
curl -X POST http://localhost:8000/api/attendance-reports/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 1,
    "attendance_id": 1,
    "status": true
  }'
```

### Get Student Attendance
```bash
curl http://localhost:8000/api/students/1/attendance/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### Create Timetable Entry
```bash
curl -X POST http://localhost:8000/api/timetable/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": 1,
    "course": 1,
    "session_year": 1,
    "day_of_week": "Monday",
    "start_time": "09:00",
    "end_time": "10:00",
    "room_number": "101"
  }'
```

### Create Announcement
```bash
curl -X POST http://localhost:8000/api/announcements/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Holiday Notification",
    "message": "College will be closed on January 1st",
    "target_audience": "all",
    "created_by": 1
  }'
```

---

## Pagination

All list endpoints support pagination:

```bash
GET /api/students/?page=2&page_size=10
```

Default page size: 10

---

## Filtering & Search

### Search
```bash
GET /api/students/?search=john
```

### Filter
```bash
GET /api/students/?course_id=1&gender=Male
```

### Ordering
```bash
GET /api/students/?ordering=-created_at
```

---

## Response Formats

### Success Response (List)
```json
{
    "count": 100,
    "next": "http://localhost:8000/api/students/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "full_name": "John Doe",
            "email": "john@college.edu",
            ...
        }
    ]
}
```

### Success Response (Detail)
```json
{
    "id": 1,
    "full_name": "John Doe",
    "email": "john@college.edu",
    "course_name": "Computer Science",
    ...
}
```

### Error Response
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## Status Codes

- `200 OK`: Successful GET/PUT request
- `201 Created`: Successful POST request
- `204 No Content`: Successful DELETE request
- `400 Bad Request`: Invalid data
- `401 Unauthorized`: Missing/invalid authentication
- `403 Forbidden`: No permission
- `404 Not Found`: Resource doesn't exist
- `500 Internal Server Error`: Server error

---

## Rate Limiting

API requests are rate limited to prevent abuse:
- 100 requests per hour for authenticated users
- 20 requests per hour for unauthenticated users

---

## Testing with Postman

1. Import the API collection
2. Set environment variable `BASE_URL` to `http://localhost:8000`
3. Get authentication token from `/api/auth/login/`
4. Set token in Authorization header
5. Start making requests

---

## Mobile App Integration

The API is designed for mobile app integration:

1. Authenticate user and store token securely
2. Use token in all subsequent requests
3. Handle pagination for large datasets
4. Subscribe to notifications endpoint for real-time updates
5. Implement local caching for offline support

---

## Support

For API support, contact: admin@college.edu
