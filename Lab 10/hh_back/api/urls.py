

from django.urls import path
from .views import company_detail, vacancy_list, vacancy_detail, CompanyVacanciesAPIView, CompanyListCreateAPIView, TopTenVacanciesAPIView 

urlpatterns = [
    path('companies/<int:id>/', company_detail, name='company_detail'),
    path('vacancies/', vacancy_list, name='vacancy_list'),
    path('vacancies/<int:id>/', vacancy_detail, name='vacancy_detail'),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view(), name='company_vacancies'),
    path('vacancies/top_ten/', TopTenVacanciesAPIView.as_view(), name='top_ten_vacancies'),
    path('companies/', CompanyListCreateAPIView.as_view(), name='company_list'),

]
