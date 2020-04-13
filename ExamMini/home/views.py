from django.shortcuts import render, redirect,HttpResponse
from home.models import subjects, questionPaperDetails, detailed_marks,generatebarcode
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers


def first(request):
    data = [[1,2,3],[4,5,6],[7,8,9]]
  # return render(request, 'first.html')
    return render(request, 'first.html',{'data':data})


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "admin123":
            return redirect('/link/')
        else:
            messages.error(request,"Invalid Details")
            return redirect('/adminlogin/')
    return render(request, 'adminlogin.html')

def update(request):
    if request.method=="POST":
        Evaluators=request.POST.get("evaluator")
        if Evaluators=="Evaluator 1":
            request.session['Evaluator']=1
        elif Evaluators=="Evaluator 2":
            request.session['Evaluator']=2
        else:
            request.session['Evaluator']=3
        request.session['studentid']= int(request.POST.get('studentId'))
        request.session['semid'] = request.POST.get('semester')
        request.session['subid'] = request.POST.get('subcode')
        request.session['1a']=request.POST.get("q301")
        request.session['1b']=request.POST.get('q302')
        request.session['1c']=request.POST.get('q303')
        request.session['1d']=request.POST.get('q304')
        request.session['total1']=request.POST.get('Total1')
        request.session['2a']=request.POST.get('q311')
        request.session['2b']=request.POST.get('q312')
        request.session['2c']=request.POST.get('q313')
        request.session['2d']=request.POST.get('q314')
        request.session['total2']=request.POST.get('Total2')
        request.session['maxtotal1'] = request.POST.get('maxtotal1')
        request.session['3a']=request.POST.get('q321')
        request.session['3b']=request.POST.get('q322')
        request.session['3c']=request.POST.get('q323')
        request.session['3d']=request.POST.get('q324')
        request.session['total3']=request.POST.get('Total3')
        request.session['4a']=request.POST.get('q331')
        request.session['4b']=request.POST.get('q332')
        request.session['4c']=request.POST.get('q333')
        request.session['4d']=request.POST.get('q334')
        request.session['total4']=request.POST.get('Total4')
        request.session['maxtotal2'] = request.POST.get('maxtotal2')
        request.session['5a']=request.POST.get('q341')
        request.session['5b']=request.POST.get('q342')
        request.session['5c']=request.POST.get('q343')
        request.session['5d']=request.POST.get('q344')
        request.session['total5']=request.POST.get('Total5')
        request.session['6a']=request.POST.get('q351')
        request.session['6b']=request.POST.get('q352')
        request.session['6c']=request.POST.get('q353')
        request.session['6d']=request.POST.get('q354')
        request.session['total6']=request.POST.get('Total6')
        request.session['maxtotal3'] = request.POST.get('maxtotal3')
        request.session['7a']=request.POST.get('q361')
        request.session['7b']=request.POST.get('q362')
        request.session['7c']=request.POST.get('q363')
        request.session['7d']=request.POST.get('q364')
        request.session['total7']=request.POST.get('Total7')
        request.session['8a']=request.POST.get('q371')
        request.session['8b']=request.POST.get('q372')
        request.session['8c']=request.POST.get('q373')
        request.session['8d']=request.POST.get('q374')
        request.session['total8']=request.POST.get('Total8')
        request.session['maxtotal4'] = request.POST.get('maxtotal4')
        request.session['9a']=request.POST.get('q381')
        request.session['9b']=request.POST.get('q382')
        request.session['9c']=request.POST.get('q383')
        request.session['9d']=request.POST.get('q384')
        request.session['total9']=request.POST.get('Total9')
        request.session['10a']=request.POST.get('q391')
        request.session['10b']=request.POST.get('q392')
        request.session['10c']=request.POST.get('q393')
        request.session['10d']=request.POST.get('q394')
        request.session['total10']=request.POST.get('Total10')
        request.session['maxtotal5'] = request.POST.get('maxtotal5')
        request.session['final'] =request.POST.get('FinalTotal')
        # DELETEING THE ALREADY EXISTING DETAILS OF A PARTICULAR STUDENT
        check = None
        try:
            check = detailed_marks.objects.filter(studentid=request.session['studentid'],semid=request.session['semid'],sub_id_id=request.session['subid'],Evaluator=request.session['Evaluator'])
        except:
            check = None
        if check:
            check.delete()
        else:
            messages.error(request,'This particular students marks had not been evaluated still.To add go to respected evaluator portal')
            return HttpResponseRedirect('/')
        #detailed_marks.objects.filter(studentid=request.session['studentid'],semid=request.session['semid'],sub_id_id=request.session['subid'],Evaluator=request.session['Evaluator']).delete()
       
        # request.session['Evaluator']=request.POST.get('Evaluator')
        logs = detailed_marks.objects.create(
            studentid=request.session['studentid'],semid=request.session['semid'],sub_id_id=request.session['subid'],
            a1=request.session['1a'],b1=request.session['1b'],c1=request.session['1c'],d1=request.session['1d'],total1=request.session['total1'],a2=request.session['2a'],b2=request.session['2b'],c2=request.session['2c'],d2=request.session['2d'],total2=request.session['total2'],max1=request.session['maxtotal1'],
            a3=request.session['3a'],b3=request.session['3b'],c3=request.session['3c'],d3=request.session['3d'],total3=request.session['total3'],a4=request.session['4a'],b4=request.session['4b'],c4=request.session['4c'],d4=request.session['4d'],total4=request.session['total4'],max2=request.session['maxtotal2'],
            a5=request.session['5a'],b5=request.session['5b'],c5=request.session['5c'],d5=request.session['5d'],total5=request.session['total5'],a6=request.session['6a'],b6=request.session['6b'],c6=request.session['6c'],d6=request.session['6d'],total6=request.session['total6'],max3=request.session['maxtotal3'],
            a7=request.session['7a'],b7=request.session['7b'],c7=request.session['7c'],d7=request.session['7d'],total7=request.session['total7'],a8=request.session['8a'],b8=request.session['8b'],c8=request.session['8c'],d8=request.session['8d'],total8=request.session['total8'],max4=request.session['maxtotal4'],
            a9=request.session['9a'],b9=request.session['9b'],c9=request.session['9c'],d9=request.session['9d'],total9=request.session['total9'],a10=request.session['10a'],b10=request.session['10b'],c10=request.session['10c'],d10=request.session['10d'],total10=request.session['total10'],max5=request.session['maxtotal5'],
            FinalTotal=int(request.session['maxtotal5'])+int(request.session['maxtotal4'])+int(request.session['maxtotal3'])+int(request.session['maxtotal2'])+int(request.session['maxtotal1']),Evaluator= request.session['Evaluator'])
        logs.save()
        return redirect("/thankyou/")
    else:
      #  l=questionPaperDetails.objects.all() 
        ques = generatebarcode.objects.get(Barcode=12343210)
        # print(ques[0].sub_id)
        # print(type (ques[0].sub_id))
        # print(ques[0].semid)
        # print(type (ques[0].semid))
        # print(ques.sem_id)
        print(ques)
        l=questionPaperDetails.objects.filter(sub_id_id=ques.sub_id_id,sem_id=ques.semid) 
        jdata2 = serializers.serialize("json",l)
        # print(l[0])
        g=int(ques.studentid)
        dat1=l[0].sub_id_id
        dat2=l[0].sem_id
        #return render(request,"eval1.html",{'json':jdata2},{'dat':l},{'ques':ques})
        return render(request,"update.html",{'json':jdata2,'dat':l,'g':g,'dat1':dat1,'dat2':dat2})

# def readmarks1(request):
    # if request.method=="POST":
    #     request.session['1a']=request.POST.get('q01')
    #     request.session['1b']=request.POST.get('q02')
    #     request.session['1c']=request.POST.get('q03')
    #     request.session['1d']=request.POST.get('q04')
    #     request.session['total1']=request.POST.get('Total1')
    #     log = detailed_marks.objects.create(
    #         a1=request.session['1a'],b1=request.session['1b'],c1=request.session['1c'],d1=request.session['1d'],total1=request.session['total1']
    #     )
    #     log.save()
        # request.session['1a']=request.POST.get('q01')
        # request.session['1a']=request.POST.get('q01')
        # request.session['1a']=request.POST.get('q01')
        # request.session['1a']=request.POST.get('q01')

    # else:
    #     return render(request, 'eval1.html')

def link(request):
    return render(request, 'link.html')


# def evaluatorlogin(request):
#     if request.method=="POST":
#         request.session['username'] = request.POST.get('username')
#         request.session['password'] = request.POST.get('password')
#         if request.session['username'] == "evaluator1" and request.session['password'] == "evaluator1":
#             return redirect("/eval1/")
#         elif request.session['username'] == "evaluator2" and request.session['password'] == "evaluator2":
#             return redirect("/eval2/")
#         else:
#             messages.error(request,"Invalid Details")
#             return HttpResponseRedirect("/evaluatorlogin/")
#     else:
#         return render(request, 'evaluatorlogin.html')


def question(request):
    if request.method == "POST":
        semester = request.POST.get('semester')
        request.session['branch'] = request.POST.get('branch')
        print(request.session['branch'])
        request.session['semester'] = request.POST.get('semester')
        print(request.session['semester'])
        request.session['sub_name'] = request.POST.get('sub_ids')
        abc = subjects.objects.get(sub_name=request.session['sub_name'],semester = request.session['semester'])
        request.session['sub_id']=int(abc.sub_id)

        return redirect('/questionpaper/')
    else:
        data1 = subjects.objects.all()
        datal = serializers.serialize("json",data1)
        length = data1.count()
        # ques=generate
        # print(datal, datal[1], datal[1].branch)
        return render(request, 'question.html', {'data': data1, 'datas': datal, 'length':length})


def questionpaper(request):
    if request.method == "POST":
        for i in range(1, 11):
            print("question "+str(i))
            a = request.POST.get("rad"+str(i))
            for j in range(1, int(a)+1):
                if j == 1:
                    p = request.POST.get('n'+str(i)+str(j))
                    print(p)
                elif j == 2:
                    q = request.POST.get('n'+str(i)+str(j))
                    print(q)
                elif j == 3:
                    r = request.POST.get('n'+str(i)+str(j))
                    print(r)
                else:
                    s = request.POST.get('n'+str(i)+str(j))
                    print(s)
            # print(p,q,r,s)
            if j == 1:
                print(type(request.session['sub_id']))
                log = questionPaperDetails.objects.create(
                    sqno=j, a=p, branch=request.session['branch'], 
                    semester=request.session['semester'],slNo=1,qno=i,sub_id_id=request.session['sub_id'],sem_id=2)
            elif j == 2:
                log = questionPaperDetails.objects.create(
                    sqno=j, a=p, b=q,branch=request.session['branch'],
                    semester=request.session['semester'],slNo=1, qno=i,sub_id_id=request.session['sub_id'],sem_id=2)
            elif j == 3:
                log = questionPaperDetails.objects.create(
                    sqno=j, a=p, b=q, c=r, branch=request.session['branch'],
                    semester=request.session['semester'],slNo=1,qno=i,sub_id_id=request.session['sub_id'],sem_id=2)
            else:
                log = questionPaperDetails.objects.create(
                    sqno=j, a=p, b=q, c=r,d=s, branch=request.session['branch'], 
                    semester=request.session['semester'],slNo=1,qno=i,sub_id_id=request.session['sub_id'],sem_id=2)
            log.save()
        return redirect('/thankyou/')
    else:
        return render(request, 'adminquestionsetting.html')


# def process(request):
#     semester = request.POST.get('semester')
#     branch = request.POST.get('branch')
#     data = subjects.objects.all()
#     if semester and branch:
#         return JsonResponse({'data': data})
#     return JsonResponse({'error': 'Missing data!'})




def thankyou(request):
    return render(request, 'thankyou.html')


def eval1(request):
    if request.method=="POST":
        Evaluators=request.POST.get("evaluator")
        if Evaluators=="Evaluator 1":
            request.session['Evaluator']=1
        elif Evaluators=="Evaluator 2":
            request.session['Evaluator']=2
        else:
            request.session['Evaluator']=3
        request.session['studentid']= request.POST.get('studentId')
        request.session['semid'] = request.POST.get('semester')
        request.session['subid'] = request.POST.get('subcode')
        request.session['1a']=request.POST.get("q301")
        request.session['1b']=request.POST.get('q302')
        request.session['1c']=request.POST.get('q303')
        request.session['1d']=request.POST.get('q304')
        request.session['total1']=request.POST.get('Total1')
        request.session['2a']=request.POST.get('q311')
        request.session['2b']=request.POST.get('q312')
        request.session['2c']=request.POST.get('q313')
        request.session['2d']=request.POST.get('q314')
        request.session['total2']=request.POST.get('Total2')
        request.session['maxtotal1'] = request.POST.get('maxtotal1')
        request.session['3a']=request.POST.get('q321')
        request.session['3b']=request.POST.get('q322')
        request.session['3c']=request.POST.get('q323')
        request.session['3d']=request.POST.get('q324')
        request.session['total3']=request.POST.get('Total3')
        request.session['4a']=request.POST.get('q331')
        request.session['4b']=request.POST.get('q332')
        request.session['4c']=request.POST.get('q333')
        request.session['4d']=request.POST.get('q334')
        request.session['total4']=request.POST.get('Total4')
        request.session['maxtotal2'] = request.POST.get('maxtotal2')
        request.session['5a']=request.POST.get('q341')
        request.session['5b']=request.POST.get('q342')
        request.session['5c']=request.POST.get('q343')
        request.session['5d']=request.POST.get('q344')
        request.session['total5']=request.POST.get('Total5')
        request.session['6a']=request.POST.get('q351')
        request.session['6b']=request.POST.get('q352')
        request.session['6c']=request.POST.get('q353')
        request.session['6d']=request.POST.get('q354')
        request.session['total6']=request.POST.get('Total6')
        request.session['maxtotal3'] = request.POST.get('maxtotal3')
        request.session['7a']=request.POST.get('q361')
        request.session['7b']=request.POST.get('q362')
        request.session['7c']=request.POST.get('q363')
        request.session['7d']=request.POST.get('q364')
        request.session['total7']=request.POST.get('Total7')
        request.session['8a']=request.POST.get('q371')
        request.session['8b']=request.POST.get('q372')
        request.session['8c']=request.POST.get('q373')
        request.session['8d']=request.POST.get('q374')
        request.session['total8']=request.POST.get('Total8')
        request.session['maxtotal4'] = request.POST.get('maxtotal4')
        request.session['9a']=request.POST.get('q381')
        request.session['9b']=request.POST.get('q382')
        request.session['9c']=request.POST.get('q383')
        request.session['9d']=request.POST.get('q384')
        request.session['total9']=request.POST.get('Total9')
        request.session['10a']=request.POST.get('q391')
        request.session['10b']=request.POST.get('q392')
        request.session['10c']=request.POST.get('q393')
        request.session['10d']=request.POST.get('q394')
        request.session['total10']=request.POST.get('Total10')
        request.session['maxtotal5'] = request.POST.get('maxtotal5')
        request.session['final'] =request.POST.get('FinalTotal')
        # request.session['Evaluator']=request.POST.get('Evaluator')
        check = None
        try:
            check = detailed_marks.objects.get(studentid=request.session['studentid'],semid=request.session['semid'],sub_id_id=request.session['subid'],Evaluator=request.session['Evaluator'])
        except:
            check = None
        if check:
            messages.error(request,'You have already entered marks for this student.If you want to update then contact ADMIN')
            return HttpResponseRedirect("/")
        else:
            logs = detailed_marks.objects.create(
                studentid=request.session['studentid'],semid=request.session['semid'],sub_id_id=request.session['subid'],
                a1=request.session['1a'],b1=request.session['1b'],c1=request.session['1c'],d1=request.session['1d'],total1=request.session['total1'],a2=request.session['2a'],b2=request.session['2b'],c2=request.session['2c'],d2=request.session['2d'],total2=request.session['total2'],max1=request.session['maxtotal1'],
                a3=request.session['3a'],b3=request.session['3b'],c3=request.session['3c'],d3=request.session['3d'],total3=request.session['total3'],a4=request.session['4a'],b4=request.session['4b'],c4=request.session['4c'],d4=request.session['4d'],total4=request.session['total4'],max2=request.session['maxtotal2'],
                a5=request.session['5a'],b5=request.session['5b'],c5=request.session['5c'],d5=request.session['5d'],total5=request.session['total5'],a6=request.session['6a'],b6=request.session['6b'],c6=request.session['6c'],d6=request.session['6d'],total6=request.session['total6'],max3=request.session['maxtotal3'],
                a7=request.session['7a'],b7=request.session['7b'],c7=request.session['7c'],d7=request.session['7d'],total7=request.session['total7'],a8=request.session['8a'],b8=request.session['8b'],c8=request.session['8c'],d8=request.session['8d'],total8=request.session['total8'],max4=request.session['maxtotal4'],
                a9=request.session['9a'],b9=request.session['9b'],c9=request.session['9c'],d9=request.session['9d'],total9=request.session['total9'],a10=request.session['10a'],b10=request.session['10b'],c10=request.session['10c'],d10=request.session['10d'],total10=request.session['total10'],max5=request.session['maxtotal5'],
                FinalTotal=int(request.session['maxtotal5'])+int(request.session['maxtotal4'])+int(request.session['maxtotal3'])+int(request.session['maxtotal2'])+int(request.session['maxtotal1']),Evaluator= request.session['Evaluator'])
            logs.save()
            return redirect("/thankyou/")
    else:
      #  l=questionPaperDetails.objects.all() 
        ques = generatebarcode.objects.get(Barcode='12343210')
        # print(ques[0].sub_id_id)
        # print(type (ques[0].sub_id_id))
        # print(ques[0].semid)
        # print(type (ques[0].semid))
        subcode = ques.sub_id_id
        semid1 = ques.semid
        studid1 = ques.studentid 
        l=questionPaperDetails.objects.filter(sub_id_id=ques.sub_id_id,sem_id=ques.semid) 
        jdata2 = serializers.serialize("json",l)
        print(l)
        # print(l[0])
        #return render(request,"eval1.html",{'json':jdata2},{'dat':l},{'ques':ques})
        return render(request,"eval1.html",{'json':jdata2,'dat':l,'subcode':subcode,'semid1':semid1,'studid1':studid1})


def eval2(request):
    if request.method=="POST":
        return redirect("thankyou")
    else:
        l=questionPaperDetails.objects.all()
        jdata2=serializers.serialize("json",l)
        return render(request,"eval2.html",{'json':jdata2},{'dat':l})

def eval3(request):
    if request.method=="POST":
        Evaluators=request.POST.get("evaluator")
        if Evaluators=="Evaluator 3":
            request.session['Evaluator']=3
     #   elif Evaluators=="Evaluator 1":
      #      request.session['Evaluator']=2
       # else:
        #    request.session['Evaluator']=3
        request.session['studentid']= request.POST.get('studentId')
        request.session['semid'] = request.POST.get('semester')
        request.session['subid'] = request.POST.get('subcode')
        request.session['1a']=request.POST.get("q301")
        request.session['1b']=request.POST.get('q302')
        request.session['1c']=request.POST.get('q303')
        request.session['1d']=request.POST.get('q304')
        request.session['total1']=request.POST.get('Total1')
        request.session['2a']=request.POST.get('q311')
        request.session['2b']=request.POST.get('q312')
        request.session['2c']=request.POST.get('q313')
        request.session['2d']=request.POST.get('q314')
        request.session['total2']=request.POST.get('Total2')
        request.session['maxtotal1'] = request.POST.get('maxtotal1')
        request.session['3a']=request.POST.get('q321')
        request.session['3b']=request.POST.get('q322')
        request.session['3c']=request.POST.get('q323')
        request.session['3d']=request.POST.get('q324')
        request.session['total3']=request.POST.get('Total3')
        request.session['4a']=request.POST.get('q331')
        request.session['4b']=request.POST.get('q332')
        request.session['4c']=request.POST.get('q333')
        request.session['4d']=request.POST.get('q334')
        request.session['total4']=request.POST.get('Total4')
        request.session['maxtotal2'] = request.POST.get('maxtotal2')
        request.session['5a']=request.POST.get('q341')
        request.session['5b']=request.POST.get('q342')
        request.session['5c']=request.POST.get('q343')
        request.session['5d']=request.POST.get('q344')
        request.session['total5']=request.POST.get('Total5')
        request.session['6a']=request.POST.get('q351')
        request.session['6b']=request.POST.get('q352')
        request.session['6c']=request.POST.get('q353')
        request.session['6d']=request.POST.get('q354')
        request.session['total6']=request.POST.get('Total6')
        request.session['maxtotal3'] = request.POST.get('maxtotal3')
        request.session['7a']=request.POST.get('q361')
        request.session['7b']=request.POST.get('q362')
        request.session['7c']=request.POST.get('q363')
        request.session['7d']=request.POST.get('q364')
        request.session['total7']=request.POST.get('Total7')
        request.session['8a']=request.POST.get('q371')
        request.session['8b']=request.POST.get('q372')
        request.session['8c']=request.POST.get('q373')
        request.session['8d']=request.POST.get('q374')
        request.session['total8']=request.POST.get('Total8')
        request.session['maxtotal4'] = request.POST.get('maxtotal4')
        request.session['9a']=request.POST.get('q381')
        request.session['9b']=request.POST.get('q382')
        request.session['9c']=request.POST.get('q383')
        request.session['9d']=request.POST.get('q384')
        request.session['total9']=request.POST.get('Total9')
        request.session['10a']=request.POST.get('q391')
        request.session['10b']=request.POST.get('q392')
        request.session['10c']=request.POST.get('q393')
        request.session['10d']=request.POST.get('q394')
        request.session['total10']=request.POST.get('Total10')
        request.session['maxtotal5'] = request.POST.get('maxtotal5')
        request.session['final'] =request.POST.get('FinalTotal')
        # request.session['Evaluator']=request.POST.get('Evaluator')
        check = None
        try:
            check = detailed_marks.objects.get(studentid=request.session['studentid'],semid=request.session['semid'],sub_id=request.session['subid'],Evaluator=request.session['Evaluator'])
        except:
            check = None
        if check:
            messages.error(request,'You have already entered marks for this student.If you want to update then contact ADMIN')
            return HttpResponseRedirect("/")
        else:
            logs = detailed_marks.objects.create(
                studentid=request.session['studentid'],semid=request.session['semid'],sub_id_id=request.session['subid'],
                a1=request.session['1a'],b1=request.session['1b'],c1=request.session['1c'],d1=request.session['1d'],total1=request.session['total1'],a2=request.session['2a'],b2=request.session['2b'],c2=request.session['2c'],d2=request.session['2d'],total2=request.session['total2'],max1=request.session['maxtotal1'],
                a3=request.session['3a'],b3=request.session['3b'],c3=request.session['3c'],d3=request.session['3d'],total3=request.session['total3'],a4=request.session['4a'],b4=request.session['4b'],c4=request.session['4c'],d4=request.session['4d'],total4=request.session['total4'],max2=request.session['maxtotal2'],
                a5=request.session['5a'],b5=request.session['5b'],c5=request.session['5c'],d5=request.session['5d'],total5=request.session['total5'],a6=request.session['6a'],b6=request.session['6b'],c6=request.session['6c'],d6=request.session['6d'],total6=request.session['total6'],max3=request.session['maxtotal3'],
                a7=request.session['7a'],b7=request.session['7b'],c7=request.session['7c'],d7=request.session['7d'],total7=request.session['total7'],a8=request.session['8a'],b8=request.session['8b'],c8=request.session['8c'],d8=request.session['8d'],total8=request.session['total8'],max4=request.session['maxtotal4'],
                a9=request.session['9a'],b9=request.session['9b'],c9=request.session['9c'],d9=request.session['9d'],total9=request.session['total9'],a10=request.session['10a'],b10=request.session['10b'],c10=request.session['10c'],d10=request.session['10d'],total10=request.session['total10'],max5=request.session['maxtotal5'],
                FinalTotal=int(request.session['maxtotal5'])+int(request.session['maxtotal4'])+int(request.session['maxtotal3'])+int(request.session['maxtotal2'])+int(request.session['maxtotal1']),Evaluator= request.session['Evaluator'])
            logs.save()
            return redirect("/thankyou/")
    else:
      #  l=questionPaperDetails.objects.all() 
        ques = generatebarcode.objects.get(Barcode=12343210)
        # print(ques[0].sub_id_id)
        # print(type (ques[0].sub_id_id))
        # print(ques[0].semid)
        # print(type (ques[0].semid))
        sem = ques.semid
        sub = ques.sub_id_id
        stu = ques.studentid
        l=questionPaperDetails.objects.filter(sub_id_id=ques.sub_id_id,sem_id=ques.semid)
        jdata2 = serializers.serialize("json",l)
        # print(l[0])
        #return render(request,"eval1.html",{'json':jdata2},{'dat':l},{'ques':ques})
        return render(request,"eval3.html",{'json':jdata2,'dat':l,'sem':sem,'sub':sub,'stu':stu})