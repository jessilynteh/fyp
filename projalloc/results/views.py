from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Students
# import pandas as pd
from io import BytesIO

def project_alloc(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # if request.method == 'POST':
    #     # Retrieve the uploaded file from the request
    #     file = request.FILES.get('file')

    #     # Read the contents of the uploaded file into a DataFrame
    #     excel_data = file.read()
    #     df = pd.read_excel(BytesIO(excel_data))

    #     # Get the number of students, projects, and choices from the DataFrame
    #     num_students = len(df)
    #     # num_projects = Project.objects.count()
    #     num_choices = df.filter(regex='Selection').shape[1]

    #     # Assign each student to their preferred projects
    #     for i in range(num_students):
    #         student_data = df.iloc[i]
    #         student_id = student_data['student_id']
    #         name = student_data['student_name']
    #         grade = student_data['grade']

    #         student, _ = Students.objects.get_or_create(student_id=student_id, defaults={'name': name, 'grade': grade})

    #         for j in range(num_choices):
    #             choice = student_data[f'Selection{j+1}']
    #             if choice > 0 and choice <= num_projects:
    #                 # project = Project.objects.get(pk=choice)
    #                 # allocation = ProjectAllocation(student=student, project=project, rank=j+1)
    #                 # allocation.save()
    #                 break

    #     # Redirect to the project allocation results view
    #     # return redirect('project_allocation_results')

    # return render(request, 'project_allocation_form.html')


def upload_file_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # if request.method == 'POST' and request.FILES.get('file'):
    #     file = request.FILES['file']
    #     # TODO: Read data from the file and redirect to the project allocation view
    # else:
    #     return render(request, 'file_upload_form.html')


