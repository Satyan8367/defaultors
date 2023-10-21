import datetime
from django.http import JsonResponse
from django.shortcuts import render


from fee.models import school, student, transaction

# Create your views here.

def school_details(request):
    schid=request.POST.get('schoolid')
    schname=request.POST.get('schoolname')
    stud_name=request.POST.get('studentname')
    sch=school(school_id=schid,school_name=schname,student_name=stud_name)
    sch.save()
    return JsonResponse("data submitted",safe=False)

def fetch_student(request):
    schid=request.POST.get('schoolid')
    data=school.objects.filter(school_id=schid)
    stu=[]
    print(datetime.datetime.now())
    due_date=datetime.datetime.now() + datetime.timedelta(days=15)
    print(due_date)
    for s in data:
        stu.append(s.student_name)
    return JsonResponse(stu,safe=False)  

def student_details(request):
    stud_id=request.POST.get('studentid')
    stud_name=request.POST.get('studentname')
    sch_id=request.POST.get('schoolid')  
    now=datetime.datetime.now()
    # start_date=now.date
    # print(start_date)
    freq_days=int(request.POST.get('freqdays'))
    due_date=datetime.datetime.now() + datetime.timedelta(days=freq_days)
    # print(due_date)
    amount=request.POST.get('amount')
    s=student(student_id=stud_id,student_name=stud_name,school_id=sch_id,start_date=now,freq_month=freq_days,due_date=due_date,amount=amount,defaultor=0)
    s.save()
    return JsonResponse("data submitted successfully ",safe=False)

def get_defaultor(request):
    curr_date=datetime.datetime.now()
    data=student.objects.all()
    l=[]
    for i in range(len(data)):
       if str(curr_date) > str(data[i].due_date):
           data[i].defaultor=1
           data[i].save()
           l.append(data[i].student_name)      
    print(l)
    return JsonResponse(l,safe=False)       

def payment(request):
    stud_id=request.POST.get('studentid')
    
    trans_id=request.POST.get('transactionid')
    amount=request.POST.get('amount')
    date=datetime.datetime.now()
    t=transaction(student_id=stud_id,transaction_id=trans_id,amount=amount,date=date)
    t.save()
    data=student.objects.get(student_id=stud_id)
    if int(amount) < data.amount:
        r_amt=data.amount - int(amount)
        data.save()
        return JsonResponse("due amount: "+str(r_amt),safe=False)
    else:
        data.defaultor=0
        data.due_date=data.due_date + datetime.timedelta(days=data.freq_month)

    data.save()
    return JsonResponse("payment successfully",safe=False)
    







