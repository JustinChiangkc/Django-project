from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def home(request):
	return render(request,'home.html',{"whatyougot":"yoyoyo"})

def count(request):
	fulltext = request.GET['fulltext']
	wordlen = len(fulltext.split())

	wordcounter = Counter(fulltext.split())
	mostcommonword, mostcommontime = wordcounter.most_common(1)[0]


	return render(request, 'count.html',{'fulltext':fulltext, 'wordlen':wordlen, 'mostcommonword':mostcommonword , 'mostcommontime':mostcommontime},)

def about(request):
	return render(request, 'about.html')