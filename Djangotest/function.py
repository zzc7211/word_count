from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def counter(request):
    texts=request.GET['text']
    total_count=len(texts)
    word_disk={}
    for word in texts:
        if word not in word_disk:
            word_disk[word]=1
        else:
            word_disk[word]+=1

    sourted_dict=sorted(word_disk.items(),key=lambda w:w[1],reverse=True)

    return render(request,'count.html',{'couont':total_count,'text':texts,'worddisk':sourted_dict})
def about(request):
    return render(request,'about.html')