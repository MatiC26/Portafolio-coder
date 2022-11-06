from django.contrib import admin
from django.urls import path
from familia_data.views import FamilyDataViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FamilyDataViews)
]



    



    
