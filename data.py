# -*- coding: utf-8 -*-
"""
--------------------------------------
Project Name: BigScreenDisplay
File Name:data.py
Author: Onway
Create Date: 2022/5/27
--------------------------------------
"""

from pymongo import MongoClient
import statsmodels.api as sm
class getData:
	def __init__(self):
		self.client = MongoClient(
			"mongodb+srv://dbh:dbh04051204@cluster0.uspgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
		self.db = self.client.coronavirus
		self.chinahistory = self.db.chinahistory
		self.worldcountry = self.db.worldcountry
		self.chinaprovince = self.db.chinaprovince

	def jsonmongodb(self):
		chinaprovincecusor = self.chinaprovince.find()
		chinaprovincelist = list(chinaprovincecusor)
		output = []
		for s in chinaprovincelist:
			output.append(
				{'name': s['name'], 'value': s['nowConfirm'], 'nowConfirm': s['nowConfirm'], 'confirm': s['confirm'],
				 'wzz': s['wzz'], 'dead': s['dead']})
		return output

	def echart1(self):
		data = {}
		data0 = self.worldcountry.find()
		data0 = list(data0)
		data0 = sorted(data0, key=lambda x: x['nowConfirm'], reverse=True)
		res1 = []
		res2 = []
		for x in data0[:8]:
			res1.append(x['name'])
			res2.append(x['nowConfirm'])
		data['name'] = res1
		data['nowConfirm'] = res2
		return data

	def echart2(self):
		history = self.chinahistory.find()
		date = []
		data = []


		return data

	def echart3(self):
		data = {}
		data0 = self.chinaprovince.find()
		data0 = list(data0)
		x11, x12, x13, x14, x15 = 0, 0, 0, 0, 0
		x21, x22, x23, x24, x25 = 0, 0, 0, 0, 0
		x31, x32, x33, x34, x35 = 0, 0, 0, 0, 0
		for x in data0:
			if x['localAdd'] == 0:
				x11 += 1
			elif 1 <= x['localAdd'] <= 99:
				x12 += 1
			elif 100 <= x['localAdd'] <= 999:
				x13 += 1
			elif 1000 <= x['localAdd'] <= 9999:
				x14 += 1
			elif 10000 <= x['localAdd']:
				x15 += 1
			if x['confirm'] == 0:
				x21 += 1
			elif 1 <= x['confirm'] <= 99:
				x22 += 1
			elif 100 <= x['confirm'] <= 999:
				x23 += 1
			elif 1000 <= x['confirm'] <= 9999:
				x24 += 1
			elif 10000 <= x['confirm']:
				x25 += 1
			if x['wzz'] == 0:
				x31 += 1
			elif 1 <= x['wzz'] <= 99:
				x32 += 1
			elif 100 <= x['wzz'] <= 999:
				x33 += 1
			elif 1000 <= x['wzz'] <= 9999:
				x34 += 1
			elif 10000 <= x['wzz']:
				x35 += 1
		data['data1'] = [{"name": "0", "value": x11}, {"name": "1-99", "value": x12}, {"name": "100-999", "value": x13},
		                 {"name": "1000-9999", "value": x14}, {"name": "10000+", "value": x15}]
		data['data2'] = [{"name": "0", "value": x21}, {"name": "1-99", "value": x22}, {"name": "100-999", "value": x23},
		                 {"name": "1000-9999", "value": x24}, {"name": "10000+", "value": x25}]
		data['data3'] = [{"name": "0", "value": x31}, {"name": "1-99", "value": x32}, {"name": "100-999", "value": x33},
		                 {"name": "1000-9999", "value": x34}, {"name": "10000+", "value": x35}]
		data['xAxis'] = ["0", "1-99", "100-999", "1000-9999", "10000+"]
		data['title']=['??????????????????','????????????','???????????????']
		return data

	def echart4(self):
		history = self.chinahistory.find()
		date = []
		data = {}
		data0 = [{}, {}]
		data0[0]["name"], data0[0]["value"] = '??????????????????', []
		data0[1]["name"], data0[1]["value"] = '??????????????????', []
		for x in history:
			date.append(x['date'])
			data0[0]['value'].append(x['confirmAdd'])
			data0[1]['value'].append(x['confirm'])
		data['xAxis'] = date
		data['name'] = ['??????????????????', '??????????????????']
		data["data0"] = data0
		return data

	def echart5(self):
		data = {}
		data0 = self.chinaprovince.find()
		data0 = list(data0)
		data0 = sorted(data0, key=lambda x: x['nowConfirm'], reverse=True)
		res1 = []
		res2 = []
		for x in data0[:8]:
			res1.append(x['name'])
			res2.append(x['nowConfirm'])
		data['name'] = res1
		data['nowConfirm'] = res2
		return data

	def echart6(self):
		color = ["01", "02", "03", "04"]
		radius = [['59%', '70%'], ['49%', '60%'], ['39%', '50%'], ['29%', '40%']]
		data0 = [
			{"name": "??????", "value": self.chinaprovince.find_one({"name": "??????"})['nowConfirm']},
			{"name": "??????", "value": self.chinaprovince.find_one({"name": "??????"})['nowConfirm']},
			{"name": "??????", "value": self.chinaprovince.find_one({"name": "??????"})['nowConfirm']},
			{"name": "??????", "value": self.chinaprovince.find_one({"name": "??????"})['nowConfirm']},
		]
		data0 = sorted(data0, key=lambda x: x["value"], reverse=True)
		for i in range(4):
			data0[i]['value2'] = data0[0]['value'] + 500 - data0[i]['value']
			data0[i]['color'] = color[i]
			data0[i]['radius'] = radius[i]
		data = {}
		data['xAxis'] = [x['name'] for x in data0]
		data["data0"] = data0
		return data

	def Title(self):
		data = {}
		data["time"] = "???????????????:" + self.db.chinaTotal.find_one({"name": "??????"})['upgradetime']
		data['counter'] = {
			"counter1": {'name': "??????????????????", 'value': self.db.chinaTotal.find_one({"name": "??????"})['nowconfirm']},
			"counter2": {'name': '??????????????????', 'value': self.db.chinaTotal.find_one({"name": "??????"})['confirm']}}
		data['title']=['?????????????????????8?????????','????????????7?????????','???2???????????????????????????','?????????????????????8?????????','???????????????????????????']
		return data
