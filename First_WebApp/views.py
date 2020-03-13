from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'key101':'Ankit Raut Want to be Devloper','key102':'Pkul Want to be Devloper'})

def result(request):
    article=request.GET['article']
    words=article.split()
    counts=len(words)
    dict_words=()
    for word in words:
        if word in dict_words:
            dict_words[word]+=1
        else:
            dict_words[word]=1
    return render(request,'result.html',{'article':article,'counts':counts,'dict_words':dict_words})


'''age = request.GET['age1']
name = request.GET['name1']
msg= f'hi {name} your age is {age}'
#return render(request,'result.html')'''
