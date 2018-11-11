import os
import time
import datetime
from selenium import webdriver

chromedriver = './chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.taobao.com')
if driver.find_element_by_link_text('亲，请登录'):
	driver.find_element_by_link_text('亲，请登录').click()

flag = True
while flag:
	try:
		driver.find_element_by_link_text('hujch3')
		flag = False
	except:
		print('waiting login...')
print('login success!')

# driver.get('https://m.tb.cn/h.3kIZAIa')
driver.get('https://item.taobao.com/item.htm?ft=t&spm=a1z10.10426-c-s.243.1.633b5d60ZCT2Mk&id=556827564717')

flag = True
while flag:
	try:
		if driver.find_element_by_link_text('立即购买'):
			driver.find_element_by_link_text('立即购买').click()
		flag = False
	except:
		print(datetime.datetime.now(), 'raw hunting..')
		time.sleep(0.001)
print('submit!')

flag = True
while flag:
	try:
		if driver.find_element_by_link_text('提交订单'):
			driver.find_element_by_link_text('提交订单').click()
		flag = False
	except:
		print('submit hunting..')
		time.sleep(0.001)
print('buy!!!')
