import json
import datetime
from django.shortcuts import render
import os
from django.http import HttpResponse
import random
import numpy as np

def productdata(request):
	if(request.method == 'POST'):
			if(os.path.exists("normalUserdata.npy")):
				os.remove("normalUser.npy")
				os.remove("volAbnormal.npy")
				os.remove("culAbnormal.npy")
				os.remove("reversePolarity.npy")
				os.remove("powerfactorabnormal.npy")
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
			normalUserdata = []
			abnormalVoldata = []
			abnormalCurdata = []
			abnormalPowerFactordata = []
			abnormalReversePodata = []
			date = []
			today = datetime.date(year1,month1,day1)
			for x in range(0,days):
				normalUserdata.insert(x,getThreeDayData())
			for x in range(0,days):
				abnormalVoldata.insert(x,getLackOfPhaseVolData())
			for x in range(0,days):
				abnormalCurdata.insert(x,getAbnormalCulData())
			for x in range(0,days):
				abnormalPowerFactordata.insert(x,getAbnormalPowerFactorData())
			for x in range(0,days):
				abnormalReversePodata.insert(x,getReversePoData())
			for x in range(0,days):
				date.insert(x,today)
				today = today + datetime.timedelta(days=1)
			np.array(date)
			status = "OK"
			np.array(normalUserdata)
			np.array(abnormalVoldata)
			np.array(abnormalCurdata)
			np.array(abnormalPowerFactordata)
			np.array(abnormalReversePodata)
			np.save("normalUser.npy",normalUserdata)
			np.save("volAbnormal.npy",abnormalVoldata)
			np.save("culAbnormal.npy",abnormalCurdata)
			np.save("powerfactorabnormal.npy",abnormalPowerFactordata)
			np.save("reversePolarity.npy",abnormalReversePodata)
			np.save("index.npy",date)
			#获取一天正常用户数据
			fileurl = 'url'
			filename = {'正常用户数据':'normalUser.npy','电压异常数据':'volAbnormal.npy','电流异常数据':'culAbnormal.npy','反极性':'reversePolarity.npy','功率因数异常':'powerfactorabnormal.npy','date':'date.npy'}
			b = {'status':status,'data':abnormalReversePodata,'filename':filename}
			c = json.dumps(b)
			return HttpResponse(c)
#正常电压
def getnormalvol(request):
	if(request.method == 'GET'):
		if(os.path.exists("normalUser.npy")):
			vol = []
			date = []
			data = np.load("normalUser.npy").tolist()
			index = np.load("index.npy").tolist()
			length1 = data.__len__()
			for x in range(0,length1):
				a = data[x][6]
				b = data[x][7]
				c = data[x][8]
				v = [a,b,c]
				vol.insert(x,v)
				date.insert(x,str(index[x]))
			code = {'status':'OK','data':vol,'index':date}
			return HttpResponse(json.dumps(code))
		else:
			code = {'status':'ERROR'}
			return HttpResponse(json.dumps(code))
#三相电压平衡度
def getVolBalance(request):
	if(request.method == 'GET'):
		if(os.path.exists("normalUser.npy")):
			vol = []
			date = []
			data = np.load("normalUser.npy").tolist()
			index = np.load("index.npy").tolist()
			length1 = data.__len__()
			for x in range(0,length1):
				k = []
				for y in range(0,24):
					a = data[x][6][y]
					b = data[x][7][y]
					c = data[x][8][y]
					vmax = max(a,b,c)
					vmin = min(a,b,c)
					vb = (vmax - vmin)/vmax
					k.insert(y,vb)
				vol.insert(x,k)
				date.insert(x,str(index[x]))
			code = {'status':'OK','data':vol,'index':date}
			return HttpResponse(json.dumps(code))
		else:
			code = {'status':'ERROR'}
			return HttpResponse(json.dumps(code))
def getnormalcur(request):
	if(request.method == 'GET'):
		if(os.path.exists("normalUser.npy")):
			vol = []
			date = []
			data = np.load("normalUser.npy").tolist()
			index = np.load("index.npy").tolist()
			length1 = data.__len__()
			for x in range(0,length1):
				a = data[x][6]
				b = data[x][7]
				c = data[x][8]
				v = [a,b,c]
				vol.insert(x,v)
				date.insert(x,str(index[x]))
			code = {'status':'OK','data':vol,'index':date}
			return HttpResponse(json.dumps(code))
		else:
			code = {'status':'ERROR'}
			return HttpResponse(json.dumps(code))
#异常电压
def getabnormalvol(request):
	if(request.method == 'GET'):
		if(os.path.exists("volAbnormal.npy")):
			vol = []
			date = []
			data = np.load("volAbnormal.npy").tolist()
			index = np.load("index.npy").tolist()
			length1 = data.__len__()
			for x in range(0,length1):
				a = data[x][15]
				b = data[x][16]
				c = data[x][17]
				v = [a,b,c]
				vol.insert(x,v)
				date.insert(x,str(index[x]))
			code = {'status':'OK','data':vol,'index':date}
			return HttpResponse(json.dumps(code))
		else:
			code = {'status':'ERROR'}
			return HttpResponse(json.dumps(code))
#异常电流
def getabnormalcur(request):
	if(request.method == 'GET'):
		if(os.path.exists("culAbnormal.npy")):
			vol = []
			date = []
			data = np.load("culAbnormal.npy").tolist()
			index = np.load("index.npy").tolist()
			length1 = data.__len__()
			for x in range(0,length1):
				a = data[x][15]
				b = data[x][16]
				c = data[x][17]
				v = [a,b,c]
				vol.insert(x,v)
				date.insert(x,str(index[x]))
			code = {'status':'OK','data':vol,'index':date}
			return HttpResponse(json.dumps(code))
		else:
			code = {'status':'ERROR'}
			return HttpResponse(json.dumps(code))
#异常功率因数
def getabnormalpowerfactor(request):
	if(request.method == 'GET'):
		if(os.path.exists("powerfactorabnormal.npy")):
			vol = []
			date = []
			data = np.load("powerfactorabnormal.npy").tolist()
			index = np.load("index.npy").tolist()
			length1 = data.__len__()
			for x in range(0,length1):
				a = data[x][21]
				b = data[x][22]
				c = data[x][23]
				v = [a,b,c]
				vol.insert(x,v)
				date.insert(x,str(index[x]))
			code = {'status':'OK','data':vol,'index':date}
			return HttpResponse(json.dumps(code))
		else:
			code = {'status':'ERROR'}
			return HttpResponse(json.dumps(code))
		
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
			#第一天的功率因数
			gs1 = []
			for x in range(0,24):
				if(x in (2,3,5,6,7,9,15,17,19,22)):
					gs1.insert(x,random.uniform(0.7,0.9))
				else:
					gs1.insert(x,random.uniform(0.9,1.0))
			#第二天的功率因数
			gs2 = []
			for x in range(0,24):
				if(x in (3,4,8,9,10,16,20)):
					gs2.insert(x,random.uniform(0.7,0.8))
				else:
					gs2.insert(x,random.uniform(0.95,1.00))
			#第三天的功率因数
			gs3 = []
			for x in range(0,24):
				if(x in (3,4,8,9,10,16,20)):
					gs3.insert(x,random.uniform(0.7,0.87))
				else:
					gs3.insert(x,random.uniform(0.96,1.00))
			gl1 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv1[x],b_dv1[x],c_dv1[x],a_c1[x],b_c1[x],c_c1[x],gs1[x])
				gl1.insert(x,gl)
			gl2 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv2[x],b_dv2[x],c_dv2[x],a_c2[x],b_c2[x],c_c2[x],gs2[x])
				gl2.insert(x,gl)
			gl3 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv3[x],b_dv3[x],c_dv3[x],a_c3[x],b_c3[x],c_c3[x],gs3[x])
				gl3.insert(x,gl)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#电压异常用户数据生成函数（缺项）
def getLackOfPhaseVolData():
			random.seed()
			#随机生成a相一天电压数据
			phaseint = random.randint(0,2)

			a_dv1 = []
			if(phaseint == 1):
				a_dv1 = [0]*24
			else:
				for x in range(0,24):
					a_dv1.insert(x,random.uniform(0.99,1.00))
			#随机生成b相一天电压数据
			b_dv1 = []
			if(phaseint == 1):
				b_dv1 = [0]*24
			else:
				for x in range(0,24):
					b_dv1.insert(x,random.uniform(0.99,1.00))
			#随机生成c相电压一天数据
			c_dv1 = []
			if(phaseint == 2):
				c_dv1 = [0]*24
			else:
				for x in range(0,24):
					c_dv1.insert(x,random.uniform(0.98,1.00))
			#第二天a相电压数据
			a_dv2 = []
			if(phaseint == 0):
				a_dv2 = [0]*24
			else:
				for x in range(0,24):
					a_dv2.insert(x,random.uniform(0.96,1.00))
			#第二天的b相电压
			b_dv2 = []
			if(phaseint == 1):
				b_dv2 = [0]*24
			else:
				for x in range(0,24):
					b_dv2.insert(x,random.uniform(0.97,1.00))
			#第二天的c相电压
			c_dv2 = []
			if(phaseint == 2):
				c_dv2 = [0]*24
			else:
				for x in range(0,24):
					c_dv2.insert(x,random.uniform(0.98,1.00))
			#第三天的a相电压
			a_dv3 = []
			if(phaseint == 0):
				a_dv3 = [0]*24
			else:
				for x in range(0,24):
					a_dv3.insert(x,random.uniform(0.98,1.00))
			#第三天的b相电压
			b_dv3 = []
			if(phaseint == 1):
				b_dv3 = [0]*24
			else:
				for x in range(0,24):
					b_dv3.insert(x,random.uniform(0.96,1.00))
			#第三天的c相电压
			c_dv3 = []
			if(phaseint == 2):
				c_dv3 = [0]*24
			else:
				for x in range(0,24):
					c_dv3.insert(x,random.uniform(0.97,1.00))
			#第一天的a相电流
			a_c1 = []
			for x in range(0,24):
				a_c1.insert(x,random.uniform(0.05,0.3))
			#第一天的b相电流
			b_c1 = []
			for x in range(0,24):
				b_c1.insert(x,random.uniform(0.05,0.7))
			#第一天的c相电流
			c_c1 = []
			for x in range(0,24):
				c_c1.insert(x,random.uniform(0.05,0.6))
			#第二天的a相电流
			a_c2 = []
			for x in range(0,24):
					a_c2.insert(x,random.uniform(0.05,0.5))
			#第二天的b相电流
			b_c2 = []
			for x in range(0,24):
				b_c2.insert(x,random.uniform(0.04,0.6))
			#第二天的c相电流
			c_c2 = []
			for x in range(0,24):
				c_c2.insert(x,random.uniform(0.05,0.6))
			a_c3 = []
			for x in range(0,24):
				a_c3.insert(x,random.uniform(0.05,0.6))
			#第三天的b相电流
			b_c3 = []
			for x in range(0,24):
				b_c3.insert(x,random.uniform(0.05,0.7))
			#第三天的c相电流
			c_c3 = []
			for x in range(0,24):
				c_c3.insert(x,random.uniform(0.05,0.6))
			#第一天的功率因数
			gs1 = []
			for x in range(0,24):
					gs1.insert(x,random.uniform(0.8,1.0))
			#第二天的功率因数
			gs2 = []
			for x in range(0,24):
				gs2.insert(x,random.uniform(0.8,1.00))
			#第三天的功率因数
			gs3 = []
			for x in range(0,24):
				gs3.insert(x,random.uniform(0.9,1.00))
			#gl1 = [0]*24
			#gl2 = [0]*24
			#gl3 = [0]*24
			gl1 = []
			for x in range(0,24):
				a = a_dv1[x]
				b = b_dv1[x]
				c = c_dv1[x]
				d = a_c1[x]
				e = b_c1[x]
				f = c_c1[x]
				g = gs1[x]
				gl = CalculatePF(a,b,c,d,e,f,g)
				gl1.insert(x,gl)
			gl2 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv2[x],b_dv2[x],c_dv2[x],a_c2[x],b_c2[x],c_c2[x],gs2[x])
				gl2.insert(x,gl)
			gl3 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv3[x],b_dv3[x],c_dv3[x],a_c3[x],b_c3[x],c_c3[x],gs3[x])
				gl3.insert(x,gl)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData

def getLowVolData():
			random.seed()
			#随机生成a相一天电压数据
			phaseint1 = random.randint(0,2)

			a_dv1 = []
			if(phaseint1 == 0):
				for x in range(0,24):
					a_dv1.insert(x,random.random(0.01,0.3))
			else:
				for x in range(0,24):
					if(x in (1,2,3,4,5,6,9,11,12)):
						a_dv1.insert(x,1.00)
					else:
						a_dv1.insert(x,random.uniform(0.98,1.00))
			#随机生成b相一天电压数据
			b_dv1 = []
			if(phaseint1 == 1):
				for x in range(0,24):
					b_dv1.insert(x,random.random(0.01,0.03))
			else:
				k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
				for x in range(0,24):
					if(x in k):
						b_dv1.insert(x,1.00)
					else:
						b_dv1.insert(x,random.uniform(0.98,1.00))
			#随机生成c相电压一天数据
			c_dv1 = []
			if(phaseint1 == 2):
				for x in range(0,24):
					c_dv1.insert(x,random.random(0.01,0.2))
			else:
				k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
				for x in range(0,24):
					if(x in k):
						c_dv1.insert(x,1.00)
					else:
						c_dv1.insert(x,random.uniform(0.98,1.00))
			#第二天a相电压数据
			a_dv2 = []
			if(phaseint1 == 0):
				a_dv2.insert(x,random.random(0.01,0.3))
			else:
				k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
				for x in range(0,24):
					if(x in k):
						a_dv2.insert(x,1.00)
					else:
						a_dv2.insert(x,random.uniform(0.95,1.00))
			#第二天的b相电压
			b_dv2 = []
			if(phaseint1 == 1):
				b_dv2.insert(x,random.random(0.01,0.2))
			else:
				k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
				for x in range(0,24):	
					if(x in k):
						b_dv2.insert(x,1.00)
					else:
						b_dv2.insert(x,random.uniform(0.95,1.00))
			#第二天的c相电压
			c_dv2 = []
			if(phaseint1 == 2):
				c_dv2.insert(x,random.random(0.01,0.03))
			else:
				k = [random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23),random.randint(0,23)]
				for x in range(0,24):
					if(x in k):
						c_dv2.insert(x,1.00)
					else:
						c_dv2.insert(x,random.uniform(0.95,1.00))
			#第三天的a相电压
			a_dv3 = []
			if(phaseint1 == 0):
				a_dv3.insert(x,random.random(0.01,0.02))
			else:
				for x in range(0,24):
					a_dv3.insert(x,random.uniform(0.95,1.00))
			#第三天的b相电压
			b_dv3 = []
			if(phaseint1 == 1):
				b_dv3.insert(x,random.random(0.01,0.03))
			else:
				for x in range(0,24):
					b_dv3.insert(x,random.uniform(0.95,1.00))
			#第三天的c相电压
			c_dv3 = []
			if(phaseint1 == 2):
				c_dv3.insert(x,random.random(0.01,0.2))
			else:
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
				c = np.random.random_integers(0,23,2)
				if(x in b):
					b_c1.insert(x,random.uniform(0.05,0.15))
				elif(x in c and  not x in b ):
					b_c1.insert(x,random.uniform(0.4,0.55))
				else:
					b_c1.insert(x,random.uniform(0.15,0.3))
			#第一天的c相电流
			c_c1 = []
			for x in range(0,24):
				if(x in (2,3,6,7,8,16,19,20,22)):
					c_c1.insert(x,random.uniform(0.05,0.15))
				elif(x in (11,14)):
					c_c1.insert(x,random.uniform(0.4,0.55))
				else:
					c_c1.insert(x,random.uniform(0.15,0.3))
			#第二天的a相电流
			a_c2 = []
			for x in range(0,24):
				if(x in (3,4,7,9,10,16,19,20)):
					a_c2.insert(x,random.uniform(0.05,0.15))
				else:
					a_c2.insert(x,random.uniform(0.1,0.5))
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
			#第一天的功率因数
			gs1 = []
			for x in range(0,24):
				if(x in (2,3,5,6,7,9,15,17,19,22)):
					gs1.insert(x,random.uniform(0.7,0.9))
				else:
					gs1.insert(x,random.uniform(0.9,1.0))
			#第二天的功率因数
			gs2 = []
			for x in range(0,24):
				if(x in (3,4,8,9,10,16,20)):
					gs2.insert(x,random.uniform(0.7,0.8))
				else:
					gs2.insert(x,random.uniform(0.95,1.00))
			#第三天的功率因数
			gs3 = []
			for x in range(0,24):
				if(x in (3,4,8,9,10,16,20)):
					gs3.insert(x,random.uniform(0.7,0.87))
				else:
					gs3.insert(x,random.uniform(0.96,1.00))
			gl1 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv1[x],b_dv1[x],c_dv1[x],a_c1[x],b_c1[x],c_c1[x],gs1[x])
				gl1.insert(x,gl)
			gl2 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv2[x],b_dv2[x],c_dv2[x],a_c2[x],b_c2[x],c_c2[x],gs2[x])
				gl2.insert(x,gl)
			gl3 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv3[x],b_dv3[x],c_dv3[x],a_c3[x],b_c3[x],c_c3[x],gs3[x])
				gl3.insert(x,gl)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
def getAbnormalCulData():
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
			
			phaseint = random.randint(0,2)
			a_c1 = [] 				#第一天a相电流
			a_c2 = []				#第二天a相电流
			a_c3 = []				#第三天a相电流
			b_c1 = []				#第一天b相电流
			b_c2 = []				#第二天b相电流
			b_c3 = []				#第三天b相电流
			c_c1 = []				#第一天c相电流
			c_c2 = []				#第二天c相电流
			c_c3 = []				#第三天c相电流
			if(phaseint == 0):
				beg = random.randint(0,15)
				for x in range(0,24):
					if(x in range(beg,24)):
						a_c1.insert(x,0)
						a_c2.insert(x,0)
						a_c3.insert(x,0)
					else:
						a_c1.insert(x,random.uniform(0.01,0.6))
						a_c2.insert(x,random.uniform(0.01,0.6))
						a_c3.insert(x,random.uniform(0.01,0.6))
			else:
				for x in range(0,24):
					a_c1.insert(x,random.uniform(0.01,0.6))
					a_c2.insert(x,random.uniform(0.01,0.6))
					a_c3.insert(x,random.uniform(0.01,0.6))
			if(phaseint == 1):
				beg = random.randint(0,15)
				for x in range(0,24):
					if(x in range(beg,24)):
						b_c1.insert(x,0)
						b_c2.insert(x,0)
						b_c3.insert(x,0)
					else:
						b_c1.insert(x,random.uniform(0.01,0.7))
						b_c2.insert(x,random.uniform(0.01,0.7))
						b_c3.insert(x,random.uniform(0.01,0.7))
			else:
				for x in range(0,24):
					b_c1.insert(x,random.uniform(0.01,0.7))
					b_c2.insert(x,random.uniform(0.01,0.7))
					b_c3.insert(x,random.uniform(0.01,0.7))
			if(phaseint == 2):
				beg = random.randint(0,15)
				for x in range(0,24):
					if(x in range(beg,24)):
						c_c1.insert(x,0)
						c_c2.insert(x,0)
						c_c3.insert(x,0)
					else:
						c_c1.insert(x,random.uniform(0.01,0.7))
						c_c2.insert(x,random.uniform(0.01,0.7))
						c_c3.insert(x,random.uniform(0.01,0.7))
			else:
				for x in range(0,24):
					c_c1.insert(x,random.uniform(0.01,0.7))
					c_c2.insert(x,random.uniform(0.01,0.7))
					c_c3.insert(x,random.uniform(0.01,0.7))
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
			gl1 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv1[x],b_dv1[x],c_dv1[x],a_c1[x],b_c1[x],c_c1[x],gs1[x])
				gl1.insert(x,gl)
			gl2 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv2[x],b_dv2[x],c_dv2[x],a_c2[x],b_c2[x],c_c2[x],gs2[x])
				gl2.insert(x,gl)
			gl3 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv3[x],b_dv3[x],c_dv3[x],a_c3[x],b_c3[x],c_c3[x],gs3[x])
				gl3.insert(x,gl)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
def getAbnormalPowerFactorData():
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
			
			phaseint = random.randint(0,2)
			a_c1 = [] 				#第一天a相电流
			a_c2 = []				#第二天a相电流
			a_c3 = []				#第三天a相电流
			b_c1 = []				#第一天b相电流
			b_c2 = []				#第二天b相电流
			b_c3 = []				#第三天b相电流
			c_c1 = []				#第一天c相电流
			c_c2 = []				#第二天c相电流
			c_c3 = []				#第三天c相电流
			for x in range(0,24):
				a_c1.insert(x,random.uniform(0.01,1.0))
				a_c2.insert(x,random.uniform(0.01,1.0))
				a_c3.insert(x,random.uniform(0.01,1.0))
			
				b_c1.insert(x,random.uniform(0.01,1.0))
				b_c2.insert(x,random.uniform(0.01,1.0))
				b_c3.insert(x,random.uniform(0.01,1.0))
			
				c_c1.insert(x,random.uniform(0.01,1.0))
				c_c2.insert(x,random.uniform(0.01,1.0))
				c_c3.insert(x,random.uniform(0.01,1.0))
			#第一天的功率因数
			gs1 = []
			for x in range(0,24):
				gs1.insert(x,random.uniform(0.01,0.55))
			#第二天的功率因数
			gs2 = []
			for x in range(0,24):
				gs2.insert(x,random.uniform(0.01,0.55))
			#第三天的功率因数
			gs3 = []
			for x in range(0,24):
				gs3.insert(x,random.uniform(0.01,0.55))
			gl1 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv1[x],b_dv1[x],c_dv1[x],a_c1[x],b_c1[x],c_c1[x],gs1[x])
				gl1.insert(x,gl)
			gl2 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv2[x],b_dv2[x],c_dv2[x],a_c2[x],b_c2[x],c_c2[x],gs2[x])
				gl2.insert(x,gl)
			gl3 = []
			for x in range(0,24):
				gl = CalculatePF(a_dv3[x],b_dv3[x],c_dv3[x],a_c3[x],b_c3[x],c_c3[x],gs3[x])
				gl3.insert(x,gl)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
def getReversePoData():
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
			
			phaseint = random.randint(0,2)
			a_c1 = [] 				#第一天a相电流
			a_c2 = []				#第二天a相电流
			a_c3 = []				#第三天a相电流
			b_c1 = []				#第一天b相电流
			b_c2 = []				#第二天b相电流
			b_c3 = []				#第三天b相电流
			c_c1 = []				#第一天c相电流
			c_c2 = []				#第二天c相电流
			c_c3 = []				#第三天c相电流
			for x in range(0,24):
				a_c1.insert(x,random.uniform(0.01,1.0))
				a_c2.insert(x,random.uniform(0.01,1.0))
				a_c3.insert(x,random.uniform(0.01,1.0))
			
				b_c1.insert(x,random.uniform(0.01,1.0))
				b_c2.insert(x,random.uniform(0.01,1.0))
				b_c3.insert(x,random.uniform(0.01,1.0))
			
				c_c1.insert(x,random.uniform(0.01,0.7))
				c_c2.insert(x,random.uniform(0.01,0.7))
				c_c3.insert(x,random.uniform(0.01,0.7))
			#第一天的功率因数
			gs1 = []

			#第二天的功率因数
			gs2 = []
			#第三天的功率因数
			gs3 = []
			for x in range(0,24):
				gs1.insert(x,random.uniform(0.7,1.0))
				gs2.insert(x,random.uniform(0.7,1.0))
				gs3.insert(x,random.uniform(0.7,1.0))
			gl1 = []
			for x in range(0,24):
				gl1.insert(x,0)
			gl2 = []
			for x in range(0,24):
				gl2.insert(x,0)
			gl3 = []
			for x in range(0,24):
				gl3.insert(x,0)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
def CalculatePF(a_dv,b_dv,c_dv,a_c,b_c,c_c,gs):
	totalpower = a_dv*a_c + b_dv*b_c + c_dv*c_c
	powerfactor = totalpower*gs
	while(powerfactor>=1):
		powerfactor = powerfactor - 0.5
	return powerfactor

