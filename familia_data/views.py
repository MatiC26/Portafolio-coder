from django.shortcuts import render
from familia_data.models import FamiliaDataModel

def FamilyDataViews(request):
    dataFamily = FamiliaDataModel.objects.all()
    return render(request, 'index.html', { 'data': dataFamily })