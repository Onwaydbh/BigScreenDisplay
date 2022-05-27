# -*- coding: utf-8 -*-
"""
--------------------------------------
Project Name: BigScreenDisplay
File Name: dataCrawler.py
Author: Onway
Create Date: 2022/5/27
--------------------------------------
"""

import json

import requests
from pymongo import MongoClient
import datetime

class crawlData:
	def __init__(self):
		self.worldUrl = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'
		self.historyurl = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'
		self.provinceurl = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
		self.client = MongoClient(
			"mongodb+srv://dbh:dbh04051204@cluster0.uspgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
		self.db = self.client.coronavirus

	def get_page_world_data(self):
		response = requests.get(self.worldUrl)
		page = response.content.decode()
		page_data = json.loads(page)
		worldCountry = page_data['data']['WomAboard']
		return worldCountry

	def save_MongoDB_world(self, worldCountry):
		collection = self.db.worldcountry
		collection.delete_many({})
		for country in worldCountry:
			country_data = {
				'name': country['name'],
				'nowConfirm': country['nowConfirm'],
				'confirm': country['confirm'],
				'dead': country['dead']
			}
			collection.insert_one(country_data)

	def get_page_history_data(self):
		response = requests.get(self.historyurl)
		page = response.content.decode()
		page_data = json.loads(page)
		daily_data = page_data['data']
		return daily_data

	def save_MongoDB_history(self, daily_data):
		collection = self.db.chinahistory
		collection.delete_many({})
		daily_add=daily_data['chinaDayAddList']
		daily_data0=daily_data['chinaDayList']
		for i in range(len(daily_add)):
			day_data = {
				'date': daily_add[i]['date'],
				'confirmAdd': daily_add[i]['localConfirmadd'],
				'confirm':daily_data0[i]['localConfirm']
			}
			collection.insert_one(day_data)

	def get_page_province_data(self):
		response = requests.get(self.provinceurl)
		page = response.content.decode()
		page_data = json.loads(page)
		chinaProvince = page_data['data']['diseaseh5Shelf']['areaTree'][0]['children']
		chinaTotal = page_data['data']['diseaseh5Shelf']['chinaTotal']
		chinaProvince.append(chinaTotal)
		return chinaProvince

	def save_MongoDB_province(self, chinaProvince):
		collection1 = self.db.chinaprovince
		collection1.delete_many({})
		collection2 = self.db.chinaTotal
		collection2.delete_many({})
		time0=str(datetime.datetime.now()).split(".")[0]
		china_data = {
			'name': '中国',
			'nowconfirm': chinaProvince[-1]['nowConfirm'],
			'confirm': chinaProvince[-1]['confirm'],
			'upgradetime':time0,
		}
		collection2.insert_one(china_data)
		for province in chinaProvince[:-1]:
			province_data = {
				'name': province['name'],
				"nowConfirm": province['total']['nowConfirm'],
				'confirm': province['total']['confirm'],
				'wzz': province['total']['wzz'],
				'dead': province['total']['dead'],
				'localAdd':province['today']['confirm']
			}
			collection1.insert_one(province_data)

	def run(self):
		worldData = self.get_page_world_data()
		self.save_MongoDB_world(worldData)
		historyData = self.get_page_history_data()
		self.save_MongoDB_history(historyData)
		provinceData = self.get_page_province_data()
		self.save_MongoDB_province(provinceData)
		print("数据更新完毕")



