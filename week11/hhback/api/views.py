from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company,Vacancy
from api.serializers import VacancySerializer, CompanySerializer

def company_list(request):
    try:
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({'message': 'error'})

def company_detailed(request, id):
    try:
        company = Company.objects.get(id=id)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)
    except: 
        return JsonResponse({'message': 'error'})

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({'message': 'error'})
        
def vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse({'message': 'error'})

def vacancy_detailed(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False)
    except: 
        return JsonResponse({'message': 'error'})

def top_vacancies(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    except: 
        return JsonResponse({'message': 'error'})
