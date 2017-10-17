#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
import socket
import time

# print downloading process
def Schedule(a, b, c):
	per = 100.00*a*b/c
	if per > 100 :
		per = 100
	print '%.2f%%' % per

def readExcel(file_name):
	rb = open_workbook(file_name)
	table = rb.sheet_by_name('Sheet1')
	#print table.nrows
	for r in range(1, table.nrows):
		data = table.row_values(r)
		if not(data[3] == 1):
			#print str(table.cell(r, 3).value)
			print 'retrieving project ' + str(r) + data[0] +  '...'
			success = retrieveImage(file_name, data[0], data[1])
			wb = copy(rb)
			ws = wb.get_sheet(0)
			if success:
				ws.write(r, 3, 1)
				wb.save(file_name)
				print 'write success'
			else:
				ws.write(r, 3, 0)
				wb.save(file_name)
				print 'write success'

	print 'Successful retrieved all images!'


def retrieveImage(file_name, project_name, project_url):
	#driver = webdriver.PhantomJS(executable_path="E:\Applications\Python27\phantomjs-2.1.1-windows\phantomjs.exe")  
	driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
	driver.get(project_url)
	js1 = 'return document.body.scrollHeight'
	js2 = 'window.scrollTo(0, document.body.scrollHeight)'
	old_scroll_height = 0
	while(driver.execute_script(js1) > old_scroll_height):
	    old_scroll_height = driver.execute_script(js1)
	    driver.execute_script(js2)
	    time.sleep(3)
	#print soup
	soup = BeautifulSoup(driver.page_source, 'lxml')
	driver.quit()

	FindImages = soup.find_all(class_="project-module-image")

	#print FindImages
	count = 1
	success = False
	for div in FindImages:
		image_url = div.contents[1].contents[3].get("src")
		filename = project_name + '-' + str(count)
		tmp = image_url.split('/')
		if not(tmp[-1] == 'blank.png'):
			print 'Downloading image ' + filename + '...'
			print image_url
			try:
				urllib.urlretrieve(image_url, 'pic1/' + filename + '.jpg', Schedule)
				success = True
				pass
			except Exception as e:
				print 'Exception', str(e)
				urllib.urlretrieve(image_url, 'pic1/' + filename + '.jpg', Schedule)
				success = True
				raise
			else:
				pass
			finally:
				count = count + 1
				pass
		
	return success

socket.setdefaulttimeout(60)
readExcel('projectURL.xls')