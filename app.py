# -*- coding: utf-8 -*-
"""
--------------------------------------
Project Name: BigScreenDisplay
File Name: app.py
Author: Onway
Create Date: 2022/5/27
--------------------------------------
"""

import json
from flask import Flask, render_template, Response, jsonify
from flask_apscheduler import APScheduler
from data import  getData
from dataCrawler import crawlData
import warnings

warnings.filterwarnings("ignore")
crawl = crawlData()


class Config(object):
	JOBS = [{
		'id': 'job1',
		'func': 'app:run',
		'args': (),
		'trigger': 'cron',
		'day': '*',
		'hour': '10',
		'minute': '28'
	}
	]
	SCHEDULER_API_ENABLED = True
	SCHEDULER_API_PREFIX = '/scheduler'


def run():
	crawl.run()


app = Flask(__name__)
app.config.from_object(Config())

# 获取数据
getDataSource = getData()


@app.route("/province")
def jsonmongodb():
	output = getDataSource.jsonmongodb()
	return Response(json.dumps(output, ensure_ascii=False), mimetype='application/json')


@app.route('/echart1')
def echart1():
	data = getDataSource.echart1()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/echart2')
def echart2():
	data = getDataSource.echart2()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/echart3')
def echart3():
	data = getDataSource.echart3()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/echart4')
def echart4():
	data = getDataSource.echart4()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/echart5')
def echart5():
	data = getDataSource.echart5()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/echart6')
def echart6():
	data = getDataSource.echart6()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/')
def index():
	title='中国&国际疫情实时追踪'
	return render_template('index.html',title=title)

@app.route('/Title')
def Title():
	data=getDataSource.Title()
	return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
if __name__ == "__main__":
	app.run(debug=True)
