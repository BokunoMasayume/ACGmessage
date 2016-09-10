#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from .forms import IntForm,ChaForm,UserForm
from .models import iAnimeModel,iComicModel,iBookModel,User,Comment
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import json


def home(request):
    out=0
    if request.method=='POST':
        if request.session.get('member_id',False):
            del request.session['member_id']
        out=1    
    return render(request,'myapp/baidu.html',{'out':out})

def search(request):
    a = request.GET.get('sousuo',None)
    if a:
        aset = (Q(name__icontains=a) | Q(company__icontains=a))
        cset = (Q(name__icontains=a) | Q(author__icontains=a))
        bset = (Q(name__icontains=a) | Q(author__icontains=a)) 
        list1 = iAnimeModel.objects.filter(aset)
        list2=iComicModel.objects.filter(cset)
        list3 = iBookModel.objects.filter(bset)
    else:
        return HttpResponseRedirect('/')   
    return render(request,'myapp/index.html',{'list1':list1,'list2':list2,'list3':list3})
     

def anime(request):
    list = iAnimeModel.objects.all()
    return render(request, 'myapp/anime.html',{'list':list}) 
def comic(request):
    list = iComicModel.objects.all()
    return render(request, 'myapp/comic.html',{'list':list})

def book(request):
    list = iBookModel.objects.all()
    return render(request, 'myapp/book.html',{'list':list})
      
def check(request):
    if request.method=="POST":
        name = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if name == "administrator" and password == "12345678":
            request.session['is_admin']=True
            return HttpResponseRedirect("/updata/anime/add/")
        return render(request,'myapp/check.html',{'fail':1}) 
    return render(request,'myapp/check.html') 

def exact_anime(request,i_id):
    a = iAnimeModel.objects.get(id=i_id)
    return render(request,'myapp/exactanime.html',{'a':a})
def exact_comic(request,i_id):
    a = iComicModel.objects.get(id=i_id)
    return render(request,'myapp/exactcomic.html',{'a':a})

def exact_book(request,i_id):
    a = iBookModel.objects.get(id=i_id)
    return render(request,'myapp/exactbook.html',{'a':a})    


def login(request):
    if request.session.get('member_id',False):
        return HttpResponse("你已登录")
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['username']
            p=form.cleaned_data['password']
            a=User.objects.filter(username=n,password=p) 
            if a:
                request.session['member_id']=a[0].id
                return HttpResponse("你已登录")
            else:
                return HttpResponse("用户名或密码不正确") 
    form=UserForm()            
    return render(request,'myapp/login.html',{'form':form})

 

def register(request):
    flag=0
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            word=form.cleaned_data['password']
            c=User.objects.filter(username=name)
            if not c:
                a=User(username=name,password=word)
                a.save()
                flag=1
            else:
                flag = 2    
    else:
        form = UserForm()
    return render(request,'myapp/register.html',{'form':form,'flag':flag})        

def comment(request):
    flag=0
    error_blank=0
    if request.method=='POST':
        if request.session.get('member_id',False):
            a=User.objects.get(id=request.session['member_id'])
            name=a.username
        else:
            name='匿名用户' 
      
        summ=request.POST.get('summary',None)
        if  summ:
            a=Comment(person=name,comment=summ)
            a.save()
            flag=1
        else :
            error_blank=1
    list=Comment.objects.all()    
    return render(request,'myapp/comment.html',{'error_blank':error_blank,'flag':flag,'list':list})            











def updata_anime_add(request): 
    error=0
    if  not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        form = IntForm(request.POST)
        name = request.POST.get('name','')
        company = request.POST.get('company','')
        country = request.POST.get('country','')
        season = request.POST.get('season','') 
        key_word = request.POST.get('key_word','')
        ori_type = request.POST.get('ori_type','')
        state = request.POST.get('state','')
        summ = request.POST.get('summary','')
        patton = iAnimeModel.objects.filter(name=name)
        if form.is_valid():
            episode = form.cleaned_data['episode']
            year = form.cleaned_data['year']
            if name and company and country and season and key_word and ori_type and summ and 'img'in request.FILES and not patton:
                a = iAnimeModel(name=name,company=company,
                country=country,year=int(year),
                season=season,key_word=key_word,
                ori_type=ori_type,episode=int(episode),state=state,img=request.FILES['img'],summary=summ ) 
                a.save() 
            else:
                error=1
        else:
            error=1            

    else:
        form = IntForm()    
    return render(request,'myapp/updataanimeadd.html',{'intform':form,'error':error})          

def updata_anime_cha(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        form = ChaForm(request.POST)
        search = request.POST.get('search',None)
        name = request.POST.get('name',None)
        company = request.POST.get('company',None)
        country = request.POST.get('country',None)
        season = request.POST.get('season',None)
        key_word = request.POST.get('key_word',None)
        ori_type = request.POST.get('ori_type',None)
        if form.is_valid():
            episode = form.cleaned_data['episode']
            year = form.cleaned_data['year']       
        state = request.POST.get('state',None)
        if 'img' in request.FILES:
            img =  request.FILES['img']
        else :
            img='' 
        summ = request.POST.get('summary',None)       
        a = iAnimeModel.objects.filter(name = search)
        if a:
            a=a[0]
            if name:
                a.name =name
            if company:
                a.company=company
            if country:
                a.country=country
            if year:
                a.year=int(year)
            if season:    
                a.season=season
            if key_word:    
                a.key_word=key_word
            if ori_type:
                a.ori_type=ori_type
            if episode:
                a.episode=int(episode)
            if state==True or state==False:
                a.state=state
            if img:    
                a.img=img
            if summ:
                a.summary = summ    
            a.save()
            done=True
        else :
            return HttpResponse(u'没有找到<%s>啊'%search) 
    else:  
        form = ChaForm() 
        done=False 

    return render(request,'myapp/updataanimecha.html',{'intform':form,'done':done})  



def updata_anime_del(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        
        search = request.POST.get('search',None)

        a = iAnimeModel.objects.filter(name = search)
        if a  :
            a[0].delete()  
        else:
            return HttpResponse(u'没有找到<%s>啊'%search)
                
    return render(request,'myapp/updataanimedel.html')  


   
        
   
    
    
    
    
    
   


def updata_comic_add(request):
    error=0
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        form = IntForm(request.POST)
        name = request.POST.get('name','')
        author = request.POST.get('author','')
        company = request.POST.get('company','')
        country = request.POST.get('country','')
        key_word = request.POST.get('key_word','')
        state = request.POST.get('state','')
        summ  = request.POST.get('summary','')
        patton = iComicModel.objects.filter(name=name)
        if form.is_valid():
            episode = form.cleaned_data['episode']
            year = form.cleaned_data['year']
            if name and author and company and country and key_word and summ and 'img' in request.FILES and not patton:
                a = iComicModel(name=name,company=company,author=author,
                country=country,year=int(year),summary=summ,
                key_word=key_word,episode=int(episode),state=state,img=request.FILES['img'] ) 
                a.save() 
            else:
                error=1
        else:
            error=1              



    else:
        form = IntForm()    
    return render(request,'myapp/updatacomicadd.html',{'intform':form,'error':error})          

def updata_comic_cha(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        form = ChaForm(request.POST)
        search = request.POST.get('search',None)
        name = request.POST.get('name',None)
        author = request.POST.get('author',None)
        company = request.POST.get('company',None)
        country = request.POST.get('country',None)
        key_word = request.POST.get('key_word',None)
        if form.is_valid():
            episode = form.cleaned_data['episode']
            year = form.cleaned_data['year']       
        state = request.POST.get('state',None)
        if 'img' in request.FILES:
            img =  request.FILES['img']
        else :
            img='' 
        summ  = request.POST.get('summary',None)       
        a = iComicModel.objects.filter(name = search)
        if a:
            a=a[0]
            if name:
                a.name =name
            if company:
                a.company=company
            if country:
                a.country=country
            if year:
                a.year=int(year)
            if author:    
                a.author=author
            if key_word:    
                a.key_word=key_word
            if episode:
                a.episode=int(episode)
            if state==True or state==False:
                a.state=state
            if img:    
                a.img=img
            if summ:
                a.summary =summ    
            a.save()
            done=True
        else :
            return HttpResponse(u'没有找到<%s>啊'%search) 
    else:  
        form = ChaForm() 
        done=False 

    return render(request,'myapp/updatacomiccha.html',{'intform':form,'done':done})  



def updata_comic_del(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        
        search = request.POST.get('search',None)

        a = iComicModel.objects.filter(name = search)
        if a  :
            a[0].delete()  
        else:
            return HttpResponse('没有找到<%s>啊'%search)
                
    return render(request,'myapp/updatacomicdel.html')  






  




def updata_book_add(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    error=0
    if request.method == "POST":
        form = IntForm(request.POST)
        name = request.POST.get('name','')
        author = request.POST.get('author','')
        publisher = request.POST.get('publisher','')
        country = request.POST.get('country','')
        key_word = request.POST.get('key_word','')
        state = request.POST.get('state','')
        summ  = request.POST.get('summary','')
        patton = iBookModel.objects.filter(name=name)
        if form.is_valid():
            volume = form.cleaned_data['episode']
            year = form.cleaned_data['year']
            if name and author and publisher and country and key_word and summ and 'img' in request.FILES and not patton:
                a = iBookModel(name=name,publisher=publisher,author=author,
                country=country,year=int(year),summary=summ,
                key_word=key_word,volume=int(volume),state=state,img=request.FILES['img'] ) 
                a.save() 
            else:
                error=1
        else:
            error=1              



    else:
        form = IntForm()    
    return render(request,'myapp/updatabookadd.html',{'intform':form,'error':error})          

def updata_book_cha(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        form = ChaForm(request.POST)
        search = request.POST.get('search',None)
        name = request.POST.get('name',None)
        author = request.POST.get('author',None)
        publisher = request.POST.get('publisher',None)
        country = request.POST.get('country',None)
        key_word = request.POST.get('key_word',None)
        if form.is_valid():
            volume = form.cleaned_data['episode']
            year = form.cleaned_data['year']       
        state = request.POST.get('state',None)
        if 'img' in request.FILES:
            img =  request.FILES['img']
        else :
            img='' 
        summ  = request.POST.get('summary',None)   
        a = iBookModel.objects.filter(name = search)
        if a:
            a=a[0]
            if name:
                a.name =name
            if publisher:
                a.publisher=publisher
            if country:    
                a.country=country
            if year:
                a.year=int(year)
            if author:    
                a.author=author
            if key_word:    
                a.key_word=key_word
            if word_count:
                a.word_count=int(word_count)
            if state==True or state==False:
                a.state=state
            if img:    
                a.img=img
            if summ:
                a.summary=summ    
            a.save()
            done=True
        else :
            return HttpResponse(u'没有找到<%s>啊'%search) 
    else:  
        form = ChaForm() 
        done=False 

    return render(request,'myapp/updatabookcha.html',{'intform':form,'done':done})  



def updata_book_del(request):
    if not request.session.get('is_admin',False):
        return HttpResponse('你没有权限')
    if request.method == "POST":
        
        search = request.POST.get('search',None)

        a = iBookModel.objects.filter(name = search)
        if a  :
            a[0].delete()  
        else:
            return HttpResponse('没有找到<%s>啊'%search)
                
    return render(request,'myapp/updatabookdel.html') 




