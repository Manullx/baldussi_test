"""
URL configuration for baldussi_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import json

from django.contrib import admin
from django.urls import path

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from .baldussi_models import Users, UsersLogin, UsersAddresses


def getByGender(request):

    gender = request.GET.get('gender')

    filtered_users = Users.objects.select_related('user_login', 'user_address').filter(user_gender=gender)
    users_data = []

    for user in filtered_users:
        data = model_to_dict(user)
        data.update(model_to_dict(user.user_login))
        data.update(model_to_dict(user.user_address))
        users_data.append(data)

    return JsonResponse(users_data, safe=False)


def getByGreaterAge(request):

    age = request.GET.get('age')

    filtered_users = Users.objects.select_related('user_login', 'user_address').filter(user_age__gt=age)
    users_data = []

    for user in filtered_users:
        data = model_to_dict(user)
        data.update(model_to_dict(user.user_login))
        data.update(model_to_dict(user.user_address))
        users_data.append(data)

    return JsonResponse(users_data, safe=False)

@csrf_exempt
def postByGenderAge(request):

    request_body = json.loads(request.body)

    filtered_users = Users.objects.select_related('user_login', 'user_address').filter(
        user_gender=request_body['gender'],
        user_age=request_body['age']
    )
    users_data = []

    for user in filtered_users:
        data = model_to_dict(user)
        data.update(model_to_dict(user.user_login))
        data.update(model_to_dict(user.user_address))
        users_data.append(data)

    return JsonResponse(users_data, safe=False)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('getByGender/', getByGender),
    path('getByGreaterAge/', getByGreaterAge),
    path('postByGenderAge/', postByGenderAge)

]
