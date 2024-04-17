from django.shortcuts import render


from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from .serializers import CompanySerializer, VacancySerializer
from rest_framework.views import APIView
import json


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

class CompanyVacanciesAPIView(APIView):
    @csrf_exempt
    def get(self, request, id):
        company = get_object_or_404(Company, pk=id)
        serializer = VacancySerializer(company.vacancies.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class TopTenVacanciesAPIView(APIView):
    @csrf_exempt
    def get(self, request):
        top_vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

class CompanyListCreateAPIView(APIView):
    @csrf_exempt
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, safe=False, status=400)
