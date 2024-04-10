from django.shortcuts import render


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        data = [{'id': company.id, 'name': company.name, 'description': company.description, 'city': company.city, 'address': company.address} for company in companies]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        company = Company.objects.create(name=data.get("name"), description=data.get("description"), city=data.get("city"), address=data.get("address"))
        return JsonResponse({'id': company.id, 'name': company.name, 'description': company.description, 'city': company.city, 'address': company.address}, status=201)


@csrf_exempt
def company_detail(request, id):
    if request.method == "GET":
        company = get_object_or_404(Company, pk=id)
        data = {'id': company.id, 'name': company.name, 'description': company.description, 'city': company.city, 'address': company.address}
        return JsonResponse(data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        company = get_object_or_404(Company, pk=id)
        company.name = data.get("name")
        company.description = data.get("description")
        company.city = data.get("city")
        company.address = data.get("address")
        company.save()
        return JsonResponse({'id': company.id, 'name': company.name, 'description': company.description, 'city': company.city, 'address': company.address})
    elif request.method == "DELETE":
        company = get_object_or_404(Company, pk=id)
        company.delete()
        return JsonResponse({"deleted": True})

@csrf_exempt
def company_vacancies(request, id):
    if request.method == "GET":
        company = get_object_or_404(Company, pk=id)
        vacancies = company.vacancies.all()
        data = [{'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary} for vacancy in vacancies]
        return JsonResponse(data, safe=False)

@csrf_exempt
def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        data = [{'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary, 'company': vacancy.company.name} for vacancy in vacancies]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        company_name = data.get("company")
        company = get_object_or_404(Company, name=company_name)
        vacancy = Vacancy.objects.create(name=data.get("name"), description=data.get("description"), salary=data.get("salary"), company=company)
        return JsonResponse({'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary, 'company': vacancy.company.name}, status=201)

@csrf_exempt
def vacancy_detail(request, id):
    if request.method == "GET":
        vacancy = get_object_or_404(Vacancy, pk=id)
        data = {'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary, 'company': vacancy.company.name}
        return JsonResponse(data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        vacancy = get_object_or_404(Vacancy, pk=id)
        vacancy.name = data.get("name")
        company_name = data.get("company")
        company = get_object_or_404(Company, name=company_name)
        vacancy.description = data.get("description")
        vacancy.salary = data.get("salary")
        vacancy.company = company
        vacancy.save()
        return JsonResponse({'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary, 'company': vacancy.company.name}, status=201)
    elif request.method == "DELETE":
        vacancy = get_object_or_404(Vacancy, pk=id)
        vacancy.delete()
        return JsonResponse({"deleted": True})  

@csrf_exempt
def top_ten_vacancies(request):
    if request.method == "GET":
        top_vacancies = Vacancy.objects.order_by('-salary')[:10]
        data = [{'id': vacancy.id, 'name': vacancy.name, 'description': vacancy.description, 'salary': vacancy.salary, 'company': vacancy.company.name} for vacancy in top_vacancies]
        return JsonResponse(data, safe=False)

