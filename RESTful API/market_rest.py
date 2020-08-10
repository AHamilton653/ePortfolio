#!/usr/bin/python
import json
from bson import json_util
from bson.json_util import dumps
import bottle
from bottle import route, run, request, abort, response
from pymongo import MongoClient
from django.core.exceptions import ValidationError
import getpass

#Connect to db and set collection
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#Server side login
#p = getpass.getpass(prompt = 'Enter password: ')

#if p.lower() == 'password': 
#  print('Password accepted') 
#else: 
#  print('Password rejected') 

#Create new Stock Document
@route('/stocks/api/v1.0/createStock', method='POST')
def create_stock():
  try:
    document = request.json
    collection.save(document)
  except ValidationError as ve:
    abort(400, str(ve))
  except (TypeError, ValueError):
    print("Must be JSON compatible; document has not been inserted")
    return
  return "Document added\n" #return value of collection.save doesn't work

#Return Document for specified ticker symbol
@route('/stocks/api/v1.0/getStock', method='GET')
def read_stock():
  result = None
  try:
    query = {}
    query['Ticker'] = request.query.ticker
    result = dumps(collection.find(query)) #convert to bson
  except Exception, e:
    print e
    return
  return result

#Update Stock Document
@route('/stocks/api/v1.0/updateStock', method='PUT')
def update_stock():
  result = None
  try:
    query = {}
    myUpdate = {"$set" : {}}
    query['Ticker'] = request.query.ticker
    document = request.json
    myUpdate['$set'] = document
    result = collection.update(query, myUpdate)
  except Exception, e:
    print e
  return result

#Delete all stock documents by ticker
@route('/stocks/api/v1.0/deleteStockAll', method='DELETE')
def delete_stock_all():
  try:
    query = {}
    query['Ticker'] = request.query.ticker
    result = collection.delete_many(query)
  except Exception, e:
    print e
    return
  resultStr = "Deleted: %s\n" % result.deleted_count #return isn't working
  return resultStr

#Delete all stock documents by ticker
@route('/stocks/api/v1.0/deleteStockOne', method='DELETE')
def delete_stock_one():
  try:
    query = {}
    query['Ticker'] = request.query.ticker
    result = collection.delete_one(query)
  except Exception, e:
    print e
    return
  resultStr = "Deleted: %s\n" % result.deleted_count #return isn't working
  return resultStr

#Generate Stock Report from list
@route('/stocks/api/v1.0/stockReport', method='POST')
def report_stock():
  result = None
  try:
    tick_list = request.json
    query = {"Ticker" : {"$in" : tick_list}}
    result = dumps(collection.find(query))
  except Exception, e:
    print e
    return
  return result

#Return top five priced stocks for chosen industry
@route('/stocks/api/v1.0/industryReport', method='GET')
def industry_stock():
  result = None
  try:
    query = {}
    query['Industry'] = request.query.industry
    result = dumps(collection.find(query, {"Ticker" : 1, "Price" : 1, "Industry" : 1, "_id" : 0}).sort("Price", -1).limit(5))
  except Exception, e:
    print e
    return
  return result

#Return investment portfolio for selected company
@route('/stocks/api/v1.0/portfolio', method='GET')
def portfolio_stock():
  result = None
  companies = db['companies']
  try:
    query = {}
    query['name'] = request.query.company_name
    result = dumps(collection.find(query, {"name" : 1, "investments" : 1, "_id" : 0}))
  except Exception, e:
    print e
    return
  return result

if __name__ == '__main__':
#app.run(debug=True)
  run(host='localhost', port=8080)