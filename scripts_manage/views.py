from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from scripts_manage.script import Script
from .upload import handle_uploaded_file
import yaml


__ALL__ = ['register_script_view', 'scripts_list_view', 'modify_script_view', 'del_script_view',]


def register_script_view(request):
    """
    脚本注册，文件上传
    :param request:
    :return:
    """
    if request.method == "POST":
        script_name = request.POST.get('script_name')
        dir_path = request.POST.get('script_env') + '/' + request.POST.get('script_type')
        config = yaml.load(open('conf/zues.yaml', 'r'), yaml.FullLoader)
        script_path = config['zues']['upload_script_path'] + '/' + dir_path.lower()
        file_name = request.FILES.get("file")
        handle_uploaded_file(request.FILES.get("file"), file_name, script_path.lower())#上传文件
        if request.POST.get('script_langue') == 'SHELL':
            script_langue = 1
        else:
            script_langue = 2
        if request.POST.get('script_type') == 'ARCHIVE':
            script_type = 1
        elif request.POST.get('script_type') == 'ETL':
            script_type = 2
        elif request.POST.get('script_type') == 'BACKUP':
            script_type = 3
        else:
            script_type = 4
        if request.POST.get('script_env') == 'PRO_ENV':
            script_env = 1
        elif request.POST.get('script_env') == 'PRE_ENV':
            script_env = 2
        else:
            script_env = 3
        desc = request.POST.get('desc')
        scriptdict = {"script_name": script_name, "script_langue": script_langue, "script_type": script_type,
                      "script_env": script_env,"script_path":script_path, "script_desc": desc}
        Script().register_script(scriptdict)
        return render(request, 'scripts-register.html', {"STATUS": "OK"})
    elif request.method == 'GET':
        return render(request, 'scripts-register.html')


def scripts_list_view(request):
    """
    查询脚本列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        script_list = Script.scripts_list()
        paginator = Paginator(script_list, 10)
        page = request.GET.get('page', 1)
        try:
            reulstlist = paginator.page(page)
        except PageNotAnInteger:
            reulstlist = paginator.page(1)
        except EmptyPage:
            reulstlist = paginator.page(paginator.num_pages)
            print(reulstlist)
        return render(request, 'scripts-list.html', {"reulstlist": reulstlist})
    elif request.method == 'POST':
        script_list = Script.scripts_list()
        paginator = Paginator(script_list, 10)
        page = request.GET.get('page')
        try:
            reulstlist = paginator.page(page)
        except PageNotAnInteger:
            reulstlist = paginator.page(1)
        except EmptyPage:
            reulstlist = paginator.page(paginator.num_pages)
        return render(request, 'scripts-list.html', {"reulstlist": reulstlist})


def script_details_view(request, script_id):
    """
    :param request:
    :return: 返回脚本详细信息
    """
    script_info = Script.script_details(script_id)
    return render(request, 'scripts-details.html', {"script_info": script_info})


def script_modify_view(request, script_id):
    """
    修改脚本信息
    :param request:
    :return:
    """
    script_info = Script.script_details(script_id)
    return render(request, 'scripts-view.html', {"script_info": script_info})


def modify_commit_view(request):
    """
    :param request:
    :return:
    """
    pass


@csrf_exempt
def del_script_view(request):
    """
    删除单独的脚本
    :param request:
    :return:
    """
    if request.method == "POST":
        script_id = request.POST.get('scriptid')
        data = Script.script_del(script_id)
        render
        return JsonResponse({"data": "","code":200,"msg":"删除成功!"})