#coding:utf-8
'''
Created on 2016年7月28日

@author: kongwentao
'''

import json
from __builtin__ import str
#json 主要包含四个方法： 
#    dump和dumps（从Python生成JSON），
#    load和loads（解析JSON成Python的数据类型）
#    dump和dumps的唯一区别是dump会生成一个类文件对象，dumps会生成字符串，
#    同理load和loads分别解析类文件对象和字符串格式的JSON
 
 
 
#load/loads
print "--------------------------json字符串和json文件的转换-----------------------"

#写
testDict = {'a':1,'b':2}
file1 = 'my.json'
fp = open(file1,'w+')
str = json.loads(testDict)
print str,type(str)
fp.write(json.loads(str))
fp.close() 

#读
file1 = 'test.json'
fp = open(file1, 'w+')
dict1 = json.dump(fp.read())
fp.close()





print "_______________________________json字符串转化为字典：json.loads_____________________________________________________________"
#''有引号，是字符串
a = '{"isOK": 1, "isRunning": "None", "isError": "None"}'

#json字符串转化为字典
b = json.loads(a)
print b["isOK"] 




#dumps/dump
print "--------------------------------------json.dumps():dic字典--》生成字符串------------------------------"
dic = { 'str': 'this is a string', 'list': [1, 2, 'a', 'b'], 'sub_dic': { 'sub_str': 'this is sub str', 'sub_list': [1, 2, 3] }, 'end': 'end' } 

tfile = 'test.json'
tfp = open(tfile, 'r')
jstr = json.dumps(dic)
obj = json.dump(dic,tfp)

print "obj",obj
print "||||",dic 
print ">>>>",jstr

 
 
print "----------------------------------------------------------------------------------"
item = {'href': [u'/search/category/2/0/r2580'], 'name': [u'\u4e09\u91cc\u5c6f']}
print item["href"][0]
print item["name"][0]







