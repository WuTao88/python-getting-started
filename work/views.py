from django.shortcuts import render
from .models import accounts,notes,talkings
from django.forms import ModelForm 
from django import forms
from django.http import HttpResponse



#form class
class accountForm(ModelForm):
    class Meta:
        model=accounts
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'password':forms.PasswordInput(attrs={}),'info':forms.Textarea(attrs={'class':'form-control'})}
class noteForm(ModelForm):    
    class Meta:
        model=notes
        fields='__all__'


class talkingForm(ModelForm):    
    class Meta:
        model=talkings
        fields='__all__'
        widgets={'content':forms.Textarea(attrs={'class':'form-control','rows':'3','style':'resize:none'})}
class searchForm(forms.Form):
    key_word=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control mr-sm-2"}))

# Create your views here.
def index(request):
    msg="Hi,freid"
    if request.method=="GET":
        data=talkings.objects.all()
        obj=talkingForm()
        searchOjb=searchForm()
        return render(request,"index.html",{"msg":msg,'talking':obj,'search':searchOjb,'data':data})
    elif request.method=="POST":
        
        search=searchForm(request.POST)
        if search.is_valid():
            kw=search.cleaned_data.get('key_word')
            data=talkings.objects.filter(content__contains=kw)
            return render(request,"index.html",{"msg":msg,"data":data})
    return render(request,"index.html",{"msg":msg})
def profile(request): 
    msg=""
    return render(request,"index.html",{"msg":msg})

def noteDeal(request):
    msg=""
    return render(request,"index.html",{"msg":msg})

def talkingDeal(request):
    msg=""
    return render(request,"index.html",{"msg":msg})
    
