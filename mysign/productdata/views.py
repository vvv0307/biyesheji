import json
from django.shortcuts import render
import numpy
from django.http import HttpResponse
import random

def productdata(request):
	if(request.method == 'GET'):
			status = "OK"
			random.seed()
			#获取三天正常用户数据
			data = getThreeDayData()
			fileurl = 'url'
			filename = ['testfile1','testfile2','testfile3','testfile4']
			b = {'status':status,'data':data,'fileurl':fileurl,'filename':filename}
			c = json.dumps(b)
			return HttpResponse(c)

#正常用户数据生成
def getThreeDayData():
			random.seed()
			#随机生成a相一天电压数据
			a_dv1 = []
			for x in range(0,24):
				a_dv1.insert(x,random.uniform(0.98,1.00))
			#随机生成b相一天电压数据
			b_dv1 = []
			for x in range(0,24):
				b_dv1.insert(x,random.uniform(0.98,1.00))
			#随机生成c相电压一天数据
			c_dv1 = []
			for x in range(0,24):
				c_dv1.insert(x,random.uniform(0.98,1.00))
			#第二天a相电压数据
			a_dv2 = []
			for x in range(0,24):
				a_dv2.insert(x,random.uniform(0.95,1.00))
			#第二天的b相电压
			b_dv2 = []
			for x in range(0,24):
				b_dv2.insert(x,random.uniform(0.95,1.00))
			#第二天的c相电压
			c_dv2 = []
			for x in range(0,24):
				c_dv2.insert(x,random.uniform(0.95,1.00))
			#第三天的a相电压
			a_dv3 = []
			for x in range(0,24):
				a_dv3.insert(x,random.uniform(0.95,1.00))
			#第三天的b相电压
			b_dv3 = []
			for x in range(0,24):
				b_dv3.insert(x,random.uniform(0.95,1.00))
			#第三天的c相电压
			c_dv3 = []
			for x in range(0,24):
				c_dv3.insert(x,random.uniform(0.95,1.00))
			#第一天的a相电流
			a_c1 = []
			for x in range(0,24):
				a_c1.insert(x,random.uniform(0.05,0.6))
			#第一天的b相电流
			b_c1 = []
			for x in range(0,24):
				if(x  in (1,2,5,7,8,15,20)):
					b_c1.insert(x,random.uniform(0.05,0.15))
				else:
					b_c1.insert(x,random.uniform(0.1,0.6))
			#第一天的c相电流
			c_c1 = []
			for x in range(0,24):
				if(x in (2,3,6,7,8,16,19,20,22)):
					c_c1.insert(x,random.uniform(0.05,0.15))
				else:
					c_c1.insert(x,random.uniform(0.1,0.6))
			#第二天的a相电流
			a_c2 = []
			for x in range(0,24):
				if(x in (3,4,7,9,10,16,19,20)):
					a_c2.insert(x,random.uniform(0.05,0.15))
				else:
					a_c2.insert(x,random.uniform(0.1,0.6))
			#第二天的b相电流
			b_c2 = []
			for x in range(0,24):
				if(x in (3,4,5,10,11,17,21)):
					b_c2.insert(x,random.uniform(0.05,0.15))
				else:
					b_c2.insert(x,random.uniform(0.1,0.6))
			#第二天的c相电流
			c_c2 = []
			for x in range(0,24):
				if(x in (1,2,6,7,8,16,17,20,21,22)):
					c_c2.insert(x,random.uniform(0.05,0.15))
				else:
					c_c2.insert(x,random.uniform(0.1,0.6))
			a_c3 = []
			for x in range(0,24):
				if(x in (2,3,5,7,8,10,16,19,22)):
					a_c3.insert(x,random.uniform(0.07,0.2))
				else:
					a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的b相电流
			b_c3 = []
			for x in range(0,24):
				if(x in (1,2,5,7,8,15,20)):
					b_c3.insert(x,random.uniform(0.1,0.6))
				else:
					b_c3.insert(x,random.uniform(0.05,0.3))
			#第三天的c相电流
			c_c3 = []
			for x in range(0,24):
				if(x in (1,2,4,6,7,19,20)):
					c_c3.insert(x,random.uniform(0.05,0.2))
				else:
					c_c3.insert(x,random.uniform(0.1,0.6))
			#第一天的总有功功率
			gl1 = []
			for x in range(0,24):
				if(0<=x<=8):
					gl1.insert(x,random.uniform(0.04,0.4))
				elif(8<x<=16):
					gl1.insert(x,random.uniform(0.3,0.5))
				else:
					gl1.insert(x,random.uniform(0.07,0.5))
			#第二天的总有功功率
			gl2 = []
			for x in range(0,24):
				if(0<=x<=8):
					gl2.insert(x,random.uniform(0.01,0.3))
				elif(8<x<=16):
					gl2.insert(x,random.uniform(0.2,0.4))
				else:
					gl2.insert(x,random.uniform(0.07,0.5))
			#第三天的总有用功率
			gl3 = []
			for x in range(0,24):
				if(0<=x<=8):
					gl3.insert(x,random.uniform(0.1,0.4))
				elif(8<x<=16):
					gl3.insert(x,random.uniform(0.05,0.5))
				else:
					gl3.insert(x,random.uniform(0.2,0.5))
			#第一天的功率因数
			gs1 = []
			for x in range(0,24):
				if(x in (2,3,5,6,7,9,15,17,19,22)):
					gs1.insert(x,random.uniform(0.5,0.9))
				else:
					gs1.insert(x,random.uniform(0.9,1.0))
			#第二天的功率因数
			gs2 = []
			for x in range(0,24):
				if(x in (3,4,8,9,10,16,20)):
					gs2.insert(x,random.uniform(0.6,0.8))
				else:
					gs2.insert(x,random.uniform(0.95,1.00))
			#第三天的功率因数
			gs3 = []
			for x in range(0,24):
				if(x in (3,4,8,9,10,16,20)):
					gs3.insert(x,random.uniform(0.67,0.87))
				else:
					gs3.insert(x,random.uniform(0.96,1.00))
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData