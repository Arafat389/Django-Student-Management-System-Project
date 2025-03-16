from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create View (Student Registration)
def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
    

# List View (Display Students)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Update View
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

# Delete View

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


