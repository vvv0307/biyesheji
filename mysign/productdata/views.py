import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def productdata(request):
	if(request.method == 'GET'):
			status = 'OK'
			data = [1,2,3,4,5,6,7]
			fileurl = 'adfsdf'
			filename = ['file1','file2','file3','file4']
			b = {'status':status,'data':data,'fileurl':fileurl,'filename':filename}
			c = json.dumps(b)
			return HttpResponse(c)