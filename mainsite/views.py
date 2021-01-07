from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import Post
import random
from datetime import datetime
from mainsite.models import AccessInfo, Branch, StoreIncome, text1, City, Keep, Human, Adopt, Died

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals())

def citykeep(request, bid=0):
    now = datetime.now()

    cities = City.objects.all()

    if bid ==0:
        data = Keep.objects.all()
    else:
        data = Keep.objects.filter(city=bid)
    title = "縣市收容數量（隻）" 
    return render(request, "keep.html", locals())

def cityhuman(request, bid=0):
    now = datetime.now()

    cities = City.objects.all()

    if bid ==0:
        data = Human.objects.all()
    else:
        data = Human.objects.filter(city=bid)
    title = "人道處理數量（隻）" 
    return render(request, "human.html", locals())

def cityadopt(request, bid=0):
    now = datetime.now()

    cities = City.objects.all()

    if bid ==0:
        data = Adopt.objects.all()
    else:
        data = Adopt.objects.filter(city=bid)
    title = "認領養數量（隻）" 
    return render(request, "adopt.html", locals())

def citydied(request, bid=0):
    now = datetime.now()

    cities = City.objects.all()

    if bid ==0:
        data = Died.objects.all()
    else:
        data = Died.objects.filter(city=bid)
    title = "所內死亡數量（隻）" 
    return render(request, "died.html", locals())

def mychart(request, bid=0):
    now = datetime.now()

    branches = Branch.objects.all()

    if bid ==0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(branch=bid)
    title = "各分店營收情形" 
    return render(request, "mychart.html", locals())

def chart(request, year=0, month=0):
    now = datetime.now()
    branches = Branch.objects.all()
    if year==0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(income_year = year)
        if month>0:
            data = data.filter(income_month = month)

    if year>0 and month>0:
        title = "{}年{}月各分店營收情形".format(year, month)   
    elif year>0:
        title = "{}年各分店營收情形".format(year) 
    else:
        title = "各分店營收情形"
    return render(request, "mychart.html", locals())


def showpost(request, slug):
    now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "post.html", locals())
    except:
        return redirect("/")

def lotto(request):
    lucky = random.randint(1, 42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))
    
    return render(request, "lotto.html", locals())

def Text1(request):
    now = datetime.now()
    try:
        orgs = text1.objects.all()
        return render(request, "text1.html", locals())
    except Exception as e:
        print(e)
        return redirect("/")

    
