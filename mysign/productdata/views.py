import json
from django.shortcuts import render
import numpy
from django.http import HttpResponse
import random
import numpy as np

def productdata(request):
	if(request.method == 'POST'):
			Postdict = request.POST
			begin = Postdict.get('begin')
			end = Postdict.get('end')
			sbegin = begin.split('/')
			send = end.split('/')
			year1 = int(sbegin[0])
			month1 = int(sbegin[1])
			day1 = int(sbegin[2])
			year2 = int(send[0])
			month2 = int(send[1])
			day2 = int(send[2])
			days = daysBetweenDates(year1,month1,day1,year2,month2,day2)
			data = [0]*days
			for x in range(0,days):
				data[x] = getThreeDayData()
			status = "OK"
			np.array(data)
			np.save("normalUser.npy",data)
			#获取一天正常用户数据
			fileurl = 'url'
			filename = ['normalUser.npy','volAbnormal.npy','culAbnormal.npy','reversePolarity.npy','powerfactorabnormal.npy']
			b = {'status':status,'data':data,'fileurl':fileurl,'filename':filename}
			c = json.dumps(b)
			return HttpResponse(c)
def isLeapYear(year):  
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0  
  
def daysInMonth(year, month):  
    if month in [1, 3, 5, 7, 8, 10, 12]:  
        return 31  
    elif month in [4, 6, 9, 11]:  
        return 30  
    else:  
        if isLeapYear(year):  
            return 29  
        else:  
            return 28  
  
def nextDay(year, month, day):  
    """Simple version: assume every month has 30 days"""  
    if day < daysInMonth(year, month):  
        return year, month, day + 1  
    else:  
        if month == 12:  
            return year + 1, 1, 1  
        else:  
            return year, month + 1, 1  
          
def dateIsBefore(year1, month1, day1, year2, month2, day2):  
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""  
    if year1 < year2:  
        return True  
    if year1 == year2:  
        if month1 < month2:  
            return True  
        if month1 == month2:  
            return day1 < day2  
    return False  
  
def daysBetweenDates(year1, month1, day1, year2, month2, day2):  
    """Returns the number of days between year1/month1/day1 
       and year2/month2/day2. Assumes inputs are valid dates 
       in Gregorian calendar."""  
    # program defensively! Add an assertion if the input is not valid!  
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)  
    days = 0  
    while dateIsBefore(year1, month1, day1, year2, month2, day2):  
        year1, month1, day1 = nextDay(year1, month1, day1)  
        days += 1  
    return days  
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
#电压异常用户数据生成函数
def getAbnormalVolData():
			random.seed()
			#随机生成a相一天电压数据
			a_dv1 = []
			for x in range(0,24):
				if(x in (1,2,3,4,5,6,9,11,12)):
					a_dv1.insert(x,1.00)
				else:
					a_dv1.insert(x,random.uniform(0.98,1.00))
			#随机生成b相一天电压数据
			b_dv1 = []
			k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
			for x in range(0,24):
				if(x in k):
					b_dv1.insert(x,1.00)
				else:
					b_dv1.insert(x,random.uniform(0.98,1.00))
			#随机生成c相电压一天数据
			c_dv1 = []
			k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
			for x in range(0,24):
				if(x in k):
					c_dv1.insert(x,1.00)
				else:
					c_dv1.insert(x,random.uniform(0.98,1.00))
			#第二天a相电压数据
			a_dv2 = []
			k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
			for x in range(0,24):
				if(x in k):
					a_dv2.insert(x,1.00)
				else:
					a_dv2.insert(x,random.uniform(0.95,1.00))
			#第二天的b相电压
			b_dv2 = []
			k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
			for x in range(0,24):	
				if(x in k):
					b_dv2.insert(x,1.00)
				else:
					b_dv2.insert(x,random.uniform(0.95,1.00))
			#第二天的c相电压
			c_dv2 = []
			k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
			for x in range(0,24):
				if(x in k):
					c_dv2.insert(x,1.00)
				else:
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
				a_c1.insert(x,random.uniform(0.05,0.3))
			#第一天的b相电流
			b_c1 = []
			for x in range(0,24):
				b = np.random.random_integers(0,23,9)
				c = np.randmom.random_integers(0,23,2)
				if(x in b):
					b_c1.insert(x,random.uniform(0.05,0.15))
				elif(x in c and  not x in b ):
					b_c1.insert(x,random.uniform(0.5,0.65))
				else:
					b_c1.insert(x,random.uniform(0.15,0.3))
			#第一天的c相电流
			c_c1 = []
			for x in range(0,24):
				if(x in (2,3,6,7,8,16,19,20,22)):
					c_c1.insert(x,random.uniform(0.05,0.15))
				elif(x in (11,14)):
					c_c1.insert(x,random.uniform(0.5,0.65))
				else:
					c_c1.insert(x,random.uniform(0.15,0.3))
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
			#gl1 = []
			#for x in range(0,24):
			#	if(0<=x<=8):
			#		gl1.insert(x,random.uniform(0.04,0.4))
			#	elif(8<x<=16):
			#		gl1.insert(x,random.uniform(0.3,0.5))
			#	else:
			#		gl1.insert(x,random.uniform(0.07,0.5))
			#第二天的总有功功率
			#gl2 = []
			#for x in range(0,24):
			#	if(0<=x<=8):
			#		gl2.insert(x,random.uniform(0.01,0.3))
			#	elif(8<x<=16):
			#		gl2.insert(x,random.uniform(0.2,0.4))
			#	else:
			#		gl2.insert(x,random.uniform(0.07,0.5))
			#第三天的总有用功率
			#gl3 = []
			#for x in range(0,24):
			#	if(0<=x<=8):
			##	elif(8<x<=16):
			#		gl3.insert(x,random.uniform(0.05,0.5))
			#	else:
			#		gl3.insert(x,random.uniform(0.2,0.5))
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
			gl1 = [0]*24
			for x in(0,24):
				gl1[x] = CalculatePF(a_dv1[x],b_dv1[x],c_dv1[x],a_c1[x],b_c1[x],c_c1[x],gs1[x])
			gl2 = [0]*24
			for x in (0,24):
				gl2[x] = CalculatePF(a_dv2[x],b_dv2[x],c_dv2[x],a_c2[x],b_c2[x],c_c2[x],gs2[x])
			gl3 = [0]*24
			for x in range(0,24):
				gl3[x] = CalculatePF(a_dv3[x],b_dv3[x],c_dv3[x],a_c3[x],b_c3[x],c_c3[x],gs3[x])
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
def CalculatePF(a_dv,b_dv,c_dv,a_c,b_c,c_c,gs):
	totalpower = a_dv*a_c + b_dv * b_c + c_dv * c_c
	powerfactor = totalpower*gs
	return powerfactor

