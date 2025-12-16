from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Student, Staff, Instructor
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

#  DASHBOARD
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# COURSE CRUD
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_add(request):
    if request.method == 'POST':
        Course.objects.create(
            name=request.POST['name'],
            duration=request.POST['duration'],
            fee=request.POST['fee']
        )
        return redirect('course_list')
    return render(request, 'course_form.html')

@login_required
def course_edit(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.name = request.POST['name']
        course.duration = request.POST['duration']
        course.fee = request.POST['fee']
        course.save()
        return redirect('course_list')
    return render(request, 'course_form.html', {'course': course})

@login_required
def course_delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('course_list')


#  STUDENT CRUD 
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# @login_required
# def student_add(request):
#     courses = Course.objects.all()
#     if request.method == 'POST':
#         Student.objects.create(
#             full_name=request.POST['full_name'],
#             email=request.POST['email'],
#             course_id=request.POST['course']
#         )
#         return redirect('student_list')
#     return render(request, 'student_form.html', {'courses': courses})

@login_required
def student_add(request):
    courses = Course.objects.all()
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        course_id = request.POST.get("course")
        if not all([full_name, email, course_id]):
            messages.error(request, "All fields are required.")
            return render(request, "student_add.html", {"courses": courses})

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            messages.error(request, "Selected course does not exist.")
            return render(request, "student_add.html", {"courses": courses})

        Student.objects.create(full_name=full_name, email=email, course=course)
        messages.success(request, "Student added successfully.")
        return redirect('student_list')

    return render(request, "student_add.html", {"courses": courses})


@login_required
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        student.full_name = request.POST['full_name']
        student.email = request.POST['email']
        student.course_id = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'student': student, 'courses': courses})

@login_required
def student_delete(request, id):
    Student.objects.filter(id=id).delete()
    return redirect('student_list')


#  STAFF CRUD
@login_required
def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff_list.html', {'staffs': staffs})

@login_required
def staff_add(request):
    if request.method == 'POST':
        Staff.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            designation=request.POST['designation'],
            salary=request.POST['salary']
        )
        return redirect('staff_list')
    return render(request, 'staff_form.html')

@login_required
def staff_edit(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == 'POST':
        staff.full_name = request.POST['full_name']
        staff.email = request.POST['email']
        staff.designation = request.POST['designation']
        staff.salary = request.POST['salary']
        staff.save()
        return redirect('staff_list')
    return render(request, 'staff_form.html', {'staff': staff})

@login_required
def staff_delete(request, id):
    Staff.objects.filter(id=id).delete()
    return redirect('staff_list')



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def collaboration(request):
    return render(request, 'collaboration.html')

@login_required
def instructor_list(request):
    return render(request, 'instructor_list.html')

# List all instructors
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors': instructors})

# Create instructor
def instructor_add(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if not full_name or not email:
            messages.error(request, "Full Name and Email are required.")
            return render(request, 'instructor_add.html')

        Instructor.objects.create(full_name=full_name, email=email, phone=phone)
        messages.success(request, "Instructor added successfully.")
        return redirect('instructor_list')

    return render(request, 'instructor_add.html')

# Update instructor
def instructor_edit(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if not full_name or not email:
            messages.error(request, "Full Name and Email are required.")
            return render(request, 'instructor_edit.html', {'instructor': instructor})

        instructor.full_name = full_name
        instructor.email = email
        instructor.phone = phone
        instructor.save()
        messages.success(request, "Instructor updated successfully.")
        return redirect('instructor_list')

    return render(request, 'instructor_edit.html', {'instructor': instructor})

# Delete instructor
def instructor_delete(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    if request.method == "POST":
        instructor.delete()
        messages.success(request, "Instructor deleted successfully.")
        return redirect('instructor_list')
    return render(request, 'instructor_delete.html', {'instructor': instructor})
