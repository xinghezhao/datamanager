import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.

def get_menu(request):
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps({'result':'not login'}), content_type="application/json")
    menu_list = []
    for menu in Menu.objects.all():
        permission = menu.permission
        if permission is None:
            continue
        for up in request.user.userpermission_set.all():
            if up.permission == permission:
                 menu_list.append(menu.title)
                 print(menu_list)
                 break
    return HttpResponse(json.dumps({'result': menu_list}), content_type="application/json")
