from django.shortcuts import render
from django.http.response import JsonResponse
import datetime


def special_case_2003(request):
    return JsonResponse({'special': 'High School 1st grade'})


def year_archive(request, year):
    return JsonResponse({'year': year})


def month_archive(request, year, month):
    return JsonResponse({'year': year, 'month': month})


def article_detail(request, year, month, slug):
    return JsonResponse({'year': year, 'month': month, 'slug': slug})
