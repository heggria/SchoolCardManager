from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, Http404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import cx_Oracle
import json
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

from .models import Collegeinfo
from .models import Studentinfo
from .models import Costinfo
from .models import Fillinfo
from .models import Majorinfo
from .models import Card
# Create your views here.

@require_http_methods(["GET"])
def show_collegeInfo(request):
    response = {}
    try:
        collegeInfos = Collegeinfo.objects.filter()
        response['list'] = json.loads(
            serializers.serialize("json", collegeInfos))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_studentInfo(request):
    response = {}
    try:
        studentInfos = Studentinfo.objects.filter()
        response['list'] = json.loads(
            serializers.serialize("json", studentInfos))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
 
def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst=Dict()
    for k,v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst

@require_http_methods(["POST"])
def get_studentInfo(request):
    response = {}
    try:
        cardI = Card.objects.all().filter(sno=request.POST.get('sno'))
        studentI = Studentinfo.objects.all().filter(sno=request.POST.get('sno'))
        response['Studentinfo'] = json.loads(serializers.serialize('json', studentI))[0]
        response['Cardinfo'] = json.loads(serializers.serialize('json', cardI))[0]
        midn=dict_to_object(json.loads(json.dumps(studentI.values("sspecial").first())))
        sspecial = dict_to_object(json.loads(serializers.serialize('json',Majorinfo.objects.all().filter(mid=midn.sspecial)))[0])

        cidn=dict_to_object(json.loads(json.dumps(studentI.values("sdept").first())))
        sdept = dict_to_object(json.loads(serializers.serialize('json',Collegeinfo.objects.all().filter(cid=cidn.sdept)))[0])

        response['sspecial'] = sspecial.fields.mname
        response['sdept'] = sdept.fields.cname

        response['error_code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response,safe=False)

#############################################

@require_http_methods(["POST"])
def login(request):
    ret = {'error_code': 0, 'msg': '登录成功'}
    try:
        user = request.POST.get('sno')
        pwd = request.POST.get('password')
        obj = Card.objects.get(sno=user,carpassword=pwd)
    except Exception as e:
        ret['error_code'] = 1
        ret['msg'] = '学号或密码错误'
    return JsonResponse(ret)

@require_http_methods(["POST"])
def registered(request):
    ret = {'error_code': 0,'msg':'注册成功！'}
    try:
        user = request.POST.get('sno')
        pwd = request.POST.get('password')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1=cursor.callfunc('sign_card',cx_Oracle.STRING,[user,pwd])
        cursor.close()
        conn.commit()
        conn.close()
        ret['cardCode'] = result1
        if(result1==''):
            ret['error_code'] = 1
        else:
            ret['msg'] = '注册失败！'
            ret['error_code'] = 0
    except Exception as e:
        ret['error_code'] = 1
        ret['msg'] = '注册失败！'
    return JsonResponse(ret)

#############################################

@require_http_methods(["POST"])
def pay(request):
    ret = {}
    try:
        sno = request.POST.get('sno')
        moeny = request.POST.get('moeny')
        passwd = request.POST.get('passwd')
        ret['sno'] = str(sno)
        ret['moeny'] = str(moeny)
        ret['password'] = str(passwd)
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1=cursor.callfunc('cost_sign',cx_Oracle.NUMBER,[sno,passwd,moeny])
        ret['result1'] = str(result1)
        cursor.close()
        conn.commit()
        conn.close()
        if(result1==0):
            ret['error_code'] = 0
            ret['msg'] = '支付成功！'
        else:
            ret['error_code'] = 1
            ret['msg'] = '金额不足或数据库操作失败！'
    except Exception as e:
        ret['error_code'] = 1
        ret['msg'] = str(e)
    return JsonResponse(ret)

@require_http_methods(["POST"])
def recharge(request):
    ret = {}
    try:
        sno = request.POST.get('sno')
        moeny = request.POST.get('moeny')
        ret['sno'] = str(sno)
        ret['moeny'] = str(moeny)
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1=cursor.callfunc('fill_sign',cx_Oracle.NUMBER,[sno,moeny])
        ret['result'] = str(result1)
        cursor.close()
        conn.commit()
        conn.close()
        if(result1==0):
            ret['error_code'] = 0
            ret['msg'] = '充值成功！'
        else:
            ret['error_code'] = 1
            ret['msg'] = '数据库操作失败！'
    except Exception as e:
        ret['error_code'] = 1
        ret['msg'] = str(e)
    return JsonResponse(ret)

########################################

@require_http_methods(["POST"])
def getExpenditureInfo(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1=cursor.callfunc('G_Cardno',cx_Oracle.STRING,[sno])
        Costinfos = Costinfo.objects.all().filter(ccardno=result1)
        response['CostInfo'] = json.loads(serializers.serialize('json', Costinfos))
        response['msg'] = 'success'
        response['error_code'] = 0
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def getIncomeInfo(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1=cursor.callfunc('G_Cardno',cx_Oracle.STRING,[sno])
        IncomeInfos = Fillinfo.objects.all().filter(rcardno=result1)
        response['IncomeInfos'] = json.loads(serializers.serialize('json', IncomeInfos))
        response['msg'] = 'success'
        response['error_code'] = 0
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)

########################################

@require_http_methods(["POST"])
def changePassword(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        password = request.POST.get('password')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1 = cursor.callfunc('Cp_sign',cx_Oracle.STRING,[sno,password])
        response['error_code'] = 0
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def RPW(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        cno = request.POST.get('cno')
        password = request.POST.get('password')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1 = cursor.callfunc('Fg_sign',cx_Oracle.STRING,[sno,cno,password])
        cursor.close()
        conn.commit()
        conn.close()
        response['error_code'] = result1
        response['sno'] = sno
        response['cno'] = cno
        response['password'] = password
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)

########################################

@require_http_methods(["POST"])
def reportLoss(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1 = cursor.callfunc('Los_sign',cx_Oracle.NUMBER,[sno])
        cursor.close()
        conn.commit()
        conn.close()
        response['sno'] = sno
        response['msg'] = 'success'
        if(result1==0):
            response['error_code'] = 0
            response['msg'] = '挂失成功！'
        else:
            response['error_code'] = 1
            response['msg'] = '数据库操作失败！'
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def cancelReportLoss(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1 = cursor.callfunc('Dele_los',cx_Oracle.NUMBER,[sno])
        cursor.close()
        conn.commit()
        conn.close()
        response['result1'] = result1
        response['msg'] = 'success'
        if(result1==0):
            response['error_code'] = 0
            response['msg'] = '取消挂失成功！'
        else:
            response['error_code'] = 1
            response['msg'] = '数据库操作失败！'
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def getReportLoss(request):
    response = {}
    try:
        sno = request.POST.get('sno')
        conn = cx_Oracle.connect('system/Abc12345@localhost:1521/orcl')
        cursor = conn.cursor()
        result1 = cursor.callfunc('Get_los',cx_Oracle.NUMBER,[sno])
        cursor.close()
        conn.commit()
        conn.close()
        response['rLCode'] = result1
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    return JsonResponse(response)