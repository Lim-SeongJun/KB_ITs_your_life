from django.shortcuts import render

# Create your views here.
# 이곳의 함수는 웹 요형 처리함수
# 첫번째 파라미터는 HttpRequest request
# 반환은 HttpRespone 객체
#   (주로 HTML문서형태, 파일다운로드, pdf, 이미지, ...)
def blog_main(request):
    # 필요한 업무코드를 실행(주로 DBMS)
    return render(request,"blog/index.html",{'msg':"HELLO DJANGO"})

def calc_1(request):
    if request.method == 'POST':
        #계산
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        opr = request.POST["opr"]
        result = eval(num1+opr+num2)
        return render(request, "blog/calc_1_form.html", {'msg':request.POST,'result':f"{num1}{opr}{num2}={result}"})
    return render(request, "blog/calc_1_form.html", {'msg':request.POST})

def calc_2(request):
    if request.method =='POST':
        stat = request.POST['stat']
        result = eval(stat)
        return render(request,"blog/calc_2_form.html",{'msg':request.POST,"result":f"{stat} = {result}"})
    return render(request, 'blog/calc_2_form.html',{'msg':request.POST})

def gugudan(request):
    if request.method == "POST":
        dan = int(request.POST["dan"])
        s = ""
        for i in range(1,10):
            s += f"{dan} * {i} = {dan*i}"
        return render(request,"blog/gugudan.html",{'msg':request.POST,"result": s})
    return render(request,"blog/gugudan.html",{'msg':request.POST,"result": s})
    
    