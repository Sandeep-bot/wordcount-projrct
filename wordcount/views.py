from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    WordDictionary = {}

    for word in wordlist:
        if word in WordDictionary:
            WordDictionary[word]+= 1
        else:
            WordDictionary[word] = 1
            Sortedlist=sorted(WordDictionary.items(),key=operator.itemgetter(1),reverse=False)
    return render(request, 'count.html',
                  {"fulltext": fulltext, 'count': len(wordlist), 'WordDictionary': WordDictionary.items(),'Sortedlist':Sortedlist})
def about(request):
    return render(request,'about.html')