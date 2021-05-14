from django.shortcuts import render
from django.http.response import JsonResponse


def report(request, id=0):
    return JsonResponse({'reportId': id})


def charge(request):
    return JsonResponse({'charge': 'charged'})
