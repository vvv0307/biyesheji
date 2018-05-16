import json
import datetime
from django.shortcuts import render
import os
from django.http import HttpResponse
import random
import numpy as np
import scipy.stats as stats

def test(request):
	if(request.method=='GET'):
		b = getNormalData33()
		code = {'status':'OK','data':b}
		response = HttpResponse(json.dumps(code),content_type='application/json');
		response['Access-Control-Allow-Origin'] = '*';
		response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
		response['Access-Control-Max-Age'] = '1000'
		response['Access-Control-Allow-Headers'] = "*"
		return response

def productdata(request):
	if(request.method == 'POST'):
			Postdict = request.POST
			#33 or 34
			type = Postdict['type']
			#数据类型
			category = Postdict['category']
			data = []
			if(type=='33'):
				#正常
				if(category=='n'):
					data = getNormalData33()
				#电压异常
				elif(category=='av'):
					data = getAbnormalVolData33()
				#电流异常
				elif(category=='ac'):
					data = getAbnormalCData33()
				#反极性
				elif(category=='r'):
					data = getRData33()
				#功率因数异常
				elif(category=='apf'):
					data = getApfData33()
			elif(type=='34'):
				#正常
				if(category=='n'):
					data = getThreeDayData()
				#电压异常
				elif(category=='av'):
					data = getAvolData()
				#电流异常
				elif(category=='ac'):
					data = getAbnormalCulData()
				#反极性
				elif(category=='r'):
					data = getReversePoData()
				#功率因数异常
				elif(category=='apf'):
					data = getAbnormalPowerFactorData()
			a = []
			a.insert(0,data)
			
			np.save("data.npy",a)
			#获取一天正常用户数据
			b = {'status':'OK','data':data}
			response = HttpResponse(json.dumps(b),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
#电压
def getvol(request):
	if(request.method == 'GET'):
		if(os.path.exists("data.npy")):
			d = np.load('data.npy').tolist()[0]
			vol = []
			if(len(d)==18):
				a1 = d[0]
				c1 = d[1]
				a2 = d[2]
				c2 = d[3]
				a3 = d[4]
				c3 = d[5]
				v1 = [a1,c1]
				v2 = [a2,c2]
				v3 = [a3,c3]
				vol.insert(1,v1)
				vol.insert(2,v2)
				vol.insert(3,v3)
			elif(len(d)==24):
				a1 = d[0]
				b1 = d[1]
				c1 = d[2]
				a2 = d[3]
				b2 = d[4]
				c2 = d[5]
				a3 = d[6]
				b3 = d[7]
				c3 = d[8]
				v1 = [a1,b1,c1]
				v2 = [a2,b2,c2]
				v3 = [a3,b3,c3]
				vol.insert(1,v1)
				vol.insert(2,v2)
				vol.insert(3,v3)
			code = {'status':'OK','data':vol}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		else:
			code = {'status':'ERROR'}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response


#电压偏离度
def getvoldevia(request):
	if(request.method == 'GET'):
		if(os.path.exists("data.npy")):
			d = np.load('data.npy').tolist()[0]
			voldevia = []
			if(len(d)==18):
				a1 = []
				for x in range(0,24):
					t = abs(d[0][x] - 1)
					a1.insert(x,t)
				c1 = []
				for x in range(0,24):
					t = abs(d[1][x] - 1)
					c1.insert(x,t)
				a2 = []
				for x in range(0,24):
					t = abs(d[2][x] - 1)
					a2.insert(x,t)
				c2 = []
				for x in range(0,24):
					t = abs(d[3][x] - 1)
					c2.insert(x,t)
				a3 = []
				for x in range(0,24):
					t = abs(d[4][x] - 1)
					a3.insert(x,t)
				c3 = []
				for x in range(0,24):
					t = abs(d[5][x] - 1)
					c3.insert(x,t)
				v1 = [a1,c1]
				v2 = [a2,c2]
				v3 = [a3,c3]
				voldevia.insert(1,v1)
				voldevia.insert(2,v2)
				voldevia.insert(3,v3)
			elif(len(d)==24):
				a1 = []
				for x in range(0,24):
					t = abs(d[0][x] - 1)
					a1.insert(x,t)
				b1 = []
				for x in range(0,24):
					t = abs(d[1][x] - 1)
					b1.insert(x,t)
				c1 = []
				for x in range(0,24):
					t = abs(d[2][x] - 1)
					c1.insert(x,t)
				a2 = []
				for x in range(0,24):
					t = abs(d[3][x] - 1)
					a2.insert(x,t)
				b2 = []
				for x in range(0,24):
					t = abs(d[4][x] - 1)
					b2.insert(x,t)
				c2 = []
				for x in range(0,24):
					t = abs(d[5][x] - 1)
					c2.insert(x,t)
				a3 = []
				for x in range(0,24):
					t = abs(d[6][x] - 1)
					a3.insert(x,t)
				b3 = []
				for x in range(0,24):
					t = abs(d[7][x] - 1)
					b3.insert(x,t)
				c3 = []
				for x in range(0,24):
					t = abs(d[8][x] - 1)
					c3.insert(x,t)
				v1 = [a1,b1,c1]
				v2 = [a2,b2,c2]
				v3 = [a3,b3,c3]
				voldevia.insert(1,v1)
				voldevia.insert(2,v2)
				voldevia.insert(3,v3)
			code = {'status':'OK','data':voldevia}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		else:
			code = {'status':'ERROR'}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response





#正常用户电流平衡度
def getCurBalance(request):
	if(request.method == 'GET'):
		if(os.path.exists("data.npy")):
			d = np.load('data.npy').tolist()[0]
			vol = []
			if(len(d)==18):
				a = []
				a1 = d[6]
				c1 = d[7]
				for x in range(0,24):
					t = (max(a1[x],c1[x])-min(a1[x],c1[x]))/max(a1[x],c1[x])
					a.insert(x,t)
				b = []
				a2 = d[8]
				c2 = d[9]
				for x in range(0,24):
					t = (max(a2[x],c2[x])-min(a2[x],c2[x]))/max(a2[x],c2[x])
					b.insert(x,t)
				c = []
				a3 = d[10]
				c3 = d[11]
				for x in range(0,24):
					t = (max(a3[x],c3[x])-min(a3[x],c3[x]))/max(a3[x],c3[x])
					c.insert(x,t)
				vol.insert(1,a)
				vol.insert(2,b)
				vol.insert(3,c)
			elif(len(d)==24):
				a = []
				a1 = d[9]
				b1 = d[10]
				c1 = d[11]
				for x in range(0,24):
					t = (max(a1[x],b1[x],c1[x])-min(a1[x],b1[x],c1[x]))/max(a1[x],b1[x],c1[x])
					a.insert(x,t)
				b = []
				a2 = d[12]
				b2 = d[13]
				c2 = d[14]
				for x in range(0,24):
					t = (max(a2[x],b2[x],c2[x])-min(a2[x],b2[x],c2[x]))/max(a2[x],b2[x],c2[x])
					b.insert(x,t)
				c = []
				a3 = d[15]
				b3 = d[16]
				c3 = d[17]
				for x in range(0,24):
					t = (max(a3[x],b3[x],c3[x])-min(a3[x],b3[x],c3[x]))/max(a3[x],b3[x],c3[x])
					c.insert(x,t)
				vol.insert(1,a)
				vol.insert(2,b)
				vol.insert(3,c)
			code = {'status':'OK','data':vol}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		else:
			code = {'status':'ERROR'}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response



#正常用户三相电压平衡度
def getVolBalance(request):
	if(request.method == 'GET'):
		if(os.path.exists("data.npy")):
			d = np.load('data.npy').tolist()[0]
			vol = []
			if(len(d)==18):
				a = []
				a1 = d[0]
				c1 = d[1]
				for x in range(0,24):
					t = (max(a1[x],c1[x])-min(a1[x],c1[x]))/max(a1[x],c1[x])
					a.insert(x,t)
				b = []
				a2 = d[2]
				c2 = d[3]
				for x in range(0,24):
					t = (max(a2[x],c2[x])-min(a2[x],c2[x]))/max(a2[x],c2[x])
					b.insert(x,t)
				c = []
				a3 = d[4]
				c3 = d[5]
				for x in range(0,24):
					t = (max(a3[x],c3[x])-min(a3[x],c3[x]))/max(a3[x],c3[x])
					c.insert(x,t)
				vol.insert(1,a)
				vol.insert(2,b)
				vol.insert(3,c)
			elif(len(d)==24):
				a = []
				a1 = d[0]
				b1 = d[1]
				c1 = d[2]
				for x in range(0,24):
					t = (max(a1[x],b1[x],c1[x])-min(a1[x],b1[x],c1[x]))/max(a1[x],b1[x],c1[x])
					a.insert(x,t)
				b = []
				a2 = d[3]
				b2 = d[4]
				c2 = d[5]
				for x in range(0,24):
					t = (max(a2[x],b2[x],c2[x])-min(a2[x],b2[x],c2[x]))/max(a2[x],b2[x],c2[x])
					b.insert(x,t)
				c = []
				a3 = d[6]
				b3 = d[7]
				c3 = d[8]
				for x in range(0,24):
					t = (max(a3[x],b3[x],c3[x])-min(a3[x],b3[x],c3[x]))/max(a3[x],b3[x],c3[x])
					c.insert(x,t)
				vol.insert(1,a)
				vol.insert(2,b)
				vol.insert(3,c)
			code = {'status':'OK','data':vol}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		else:
			code = {'status':'ERROR'}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response

#正常用户电流
def getCu(request):
	if(request.method == 'GET'):
		if(os.path.exists("data.npy")):
			d = np.load('data.npy').tolist()[0]
			vol = []
			if(len(d)==18):
				a1 = d[6]
				c1 = d[7]
				a2 = d[8]
				c2 = d[9]
				a3 = d[10]
				c3 = d[11]
				v1 = [a1,c1]
				v2 = [a2,c2]
				v3 = [a3,c3]
				vol.insert(1,v1)
				vol.insert(2,v2)
				vol.insert(3,v3)
			elif(len(d)==24):
				a1 = d[9]
				b1 = d[10]
				c1 = d[11]
				a2 = d[12]
				b2 = d[13]
				c2 = d[14]
				a3 = d[15]
				b3 = d[16]
				c3 = d[17]
				v1 = [a1,b1,c1]
				v2 = [a2,b2,c2]
				v3 = [a3,b3,c3]
				vol.insert(1,v1)
				vol.insert(2,v2)
				vol.insert(3,v3)
			code = {'status':'OK','data':vol}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		else:
			code = {'status':'ERROR'}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response


#正常用户功率因数
def getPowerFactor(request):
	if(request.method == 'GET'):
		if(os.path.exists("data.npy")):
			d = np.load('data.npy').tolist()[0]
			vol = []
			if(len(d)==18):
				v1 = d[15]
				v2 = d[16]
				v3 = d[17]
				vol.insert(1,v1)
				vol.insert(2,v2)
				vol.insert(3,v3)
			elif(len(d)==24):
				v1 = d[21]
				v2 = d[22]
				v3 = d[23]
				vol.insert(1,v1)
				vol.insert(2,v2)
				vol.insert(3,v3)
			code = {'status':'OK','data':vol}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		else:
			code = {'status':'ERROR'}
			response = HttpResponse(json.dumps(code),content_type='application/json');
			response['Access-Control-Allow-Origin'] = '*';
			response['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
			response['Access-Control-Max-Age'] = '1000'
			response['Access-Control-Allow-Headers'] = "*"
			return response
		

#34正常用户数据生成
def getThreeDayData():
			d = np.load('34gd_data.npy')
			#正常数据nd
			nd = d[0]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成b相一天电压数据
			b_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			#第二天的b相电压
			b_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv2.insert(x,rd)
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][6][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的b相电压
			b_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][7][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][8][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[0][9][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的b相电流
			b_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[0][12][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的b相电流
			b_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[0][15][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的b相电流
			b_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c3.insert(x,rd)
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][21][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][22][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][23][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][18][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][19][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][20][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#34电压异常用户数据生成函数
def getAvolData():
			d = np.load('34gd_data.npy')
			#电压异常模板数据nd
			nd = d[6]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成b相一天电压数据
			b_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			#第二天的b相电压
			b_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv2.insert(x,rd)
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][6][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的b相电压
			b_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][7][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][8][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[6][9][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的b相电流
			b_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[6][12][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的b相电流
			b_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[6][15][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的b相电流
			b_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c3.insert(x,rd)
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][21][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][22][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][23][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][18][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][19][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[6][20][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData

#34电流异常数据
def getAbnormalCulData():
			d = np.load('34gd_data.npy')
			#电压异常模板数据nd
			nd = d[8]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成b相一天电压数据
			b_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			#第二天的b相电压
			b_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv2.insert(x,rd)
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][6][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的b相电压
			b_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][7][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][8][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[8][9][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的b相电流
			b_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[8][12][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的b相电流
			b_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[8][15][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的b相电流
			b_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c3.insert(x,rd)
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][21][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][22][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][23][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][18][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][19][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[8][20][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#34功率因数异常数据
def getAbnormalPowerFactorData():
			d = np.load('34gd_data.npy')
			#电压异常模板数据nd
			nd = d[13]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成b相一天电压数据
			b_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			#第二天的b相电压
			b_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv2.insert(x,rd)
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][6][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的b相电压
			b_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][7][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][8][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[13][9][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的b相电流
			b_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[13][12][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的b相电流
			b_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[13][15][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的b相电流
			b_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c3.insert(x,rd)
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][21][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][22][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][23][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][18][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][19][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[13][20][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#34反极性数据
####
def getReversePoData():
			d = np.load('34gd_data.npy')
			#电压异常模板数据nd
			nd = d[10]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成b相一天电压数据
			b_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			#第二天的b相电压
			b_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv2.insert(x,rd)
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][6][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的b相电压
			b_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][7][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][8][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[10][9][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的b相电流
			b_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[10][12][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的b相电流
			b_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[10][15][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的b相电流
			b_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				b_c3.insert(x,rd)
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][21][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][22][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][23][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][18][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][19][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][20][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,b_dv1,c_dv1,a_dv2,b_dv2,c_dv2,a_dv3,b_dv3,c_dv3,a_c1,b_c1,c_c1,a_c2,b_c2,c_c2,a_c3,b_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#33正常数据
def getNormalData33():
			d = np.load('33gg_data.npy')
			#电压异常模板数据nd
			nd = d[0]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[0][6][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[0][8][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[0][10][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][16][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][17][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][17][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][13][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][14][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][15][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,c_dv1,a_dv2,c_dv2,a_dv3,c_dv3,a_c1,c_c1,a_c2,c_c2,a_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData

#33电压异常数据
def getAbnormalVolData33():
			d = np.load('33gg_data.npy')
			#电压异常模板数据nd
			nd = d[7]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[7][6][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[7][8][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[7][10][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][15][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][16][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][17][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][12][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][13][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[7][14][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,c_dv1,a_dv2,c_dv2,a_dv3,c_dv3,a_c1,c_c1,a_c2,c_c2,a_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#33电流异常数据
def getAbnormalCData33():
			d = np.load('33gg_data.npy')
			#电压异常模板数据nd
			nd = d[5]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[5][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[5][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[5][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[5][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[5][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[5][6][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[5][8][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[5][10][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[5][15][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][16][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][17][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][12][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][13][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[0][14][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,c_dv1,a_dv2,c_dv2,a_dv3,c_dv3,a_c1,c_c1,a_c2,c_c2,a_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#33反极性数据
def getRData33():
			d = np.load('33gg_data.npy')
			#电压异常模板数据nd
			nd = d[10]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[10][6][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[10][8][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[10][10][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][15][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][16][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][17][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][12][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][13][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[10][14][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,c_dv1,a_dv2,c_dv2,a_dv3,c_dv3,a_c1,c_c1,a_c2,c_c2,a_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
#33功率因素异常数据
def getApfData33():
			d = np.load('33gg_data.npy')
			#电压异常模板数据nd
			nd = d[11]
			#随机生成a相一天电压数据
			a_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = nd[0][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv1.insert(x,rd)
			#随机生成c相电压一天数据
			c_dv1 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][1][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv1.insert(x,rd)
			#第二天a相电压数据
			a_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][2][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv2.insert(x,rd)
			
			#第二天的c相电压
			c_dv2 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][3][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv2.insert(x,rd)
			#第三天的a相电压
			a_dv3 = []
			gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][4][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_dv3.insert(x,rd)
			#第三天的c相电压
			c_dv3 = []
			#gauss = np.random.normal(0,0.07,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][5][x], 0.07
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_dv3.insert(x,rd)
			#第一天的a相电流
			a_c1 = []
			#gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[11][6][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c1.insert(x,rd)
			#第一天的c相电流
			c_c1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c1[x]>1 else 1.2*a_c1[x]
				lower = 0.8*a_c1[x] 
				mu, sigma = a_c1[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c1.insert(x,rd)
			#第二天的a相电流
			a_c2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[11][8][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c2.insert(x,rd)
			#第二天的c相电流
			c_c2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c2[x]>1 else 1.2*a_c2[x]
				lower = 0.8*a_c2[x] 
				mu, sigma = a_c2[x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c2.insert(x,rd)
			a_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1
				lower = 0
				mu, sigma = d[11][10][x], 0.2
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				a_c3.insert(x,rd)
			#第三天的a相电流
 			#a_c3 = []
			#for x in range(0,24):
			#if(x in (2,3,5,7,8,10,16,19,22)):
			#	a_c3.insert(x,random.uniform(0.07,0.2))
			#else:
			#	a_c3.insert(x,random.uniform(0.1,0.6))
			#第三天的c相电流
			c_c3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				upper = 1 if 1.2*a_c3[x]>1 else 1.2*a_c3[x]
				lower = 0.8*a_c3[x] 
				mu, sigma = a_c3[x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				c_c3.insert(x,rd)
			#第一天的功率因数
			gs1 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][15][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs1.insert(x,rd)
			#第二天的功率因数
			gs2 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][16][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs2.insert(x,rd)
			#第三天的功率因数
			gs3 = []
			gauss = np.random.normal(0,0.2,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][17][x], 0.05
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gs3.insert(x,rd)
			gl1 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][12][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl1.insert(x,rd)
			gl2 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][13][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl2.insert(x,rd)
			gl3 = []
			gauss = np.random.normal(0,0.05,24)
			for x in range(0,24):
				lower, upper = 0, 1
				mu, sigma = d[11][14][x], 0.3
				X = stats.truncnorm(
 						   (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
				rd = X.rvs(1)[0]
				gl3.insert(x,rd)
			#三天用户总数据
			ThreeDayNormalData = [a_dv1,c_dv1,a_dv2,c_dv2,a_dv3,c_dv3,a_c1,c_c1,a_c2,c_c2,a_c3,c_c3,gl1,gl2,gl3,gs1,gs2,gs3]
			return ThreeDayNormalData
def CalculatePF(a_dv,b_dv,c_dv,a_c,b_c,c_c,gs):
	totalpower = a_dv*a_c + b_dv*b_c + c_dv*c_c
	powerfactor = totalpower*gs
	while(powerfactor>=1):
		powerfactor = powerfactor - 0.5
	return powerfactor

