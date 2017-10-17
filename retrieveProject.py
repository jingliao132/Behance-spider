#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
import re
import xlwt
import socket

# --- func definition ---
# get dynamic sources, with use of webdriver
def get_content(url, max_page):
	# visit URL
	#driver = webdriver.Firefox() 
	driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
	driver.get(url)
	max_scrollPages = max_page
	pageIndex = 0
	# perform action: scroll to the bottom of page
	js1 = 'return document.body.scrollHeight'
	js2 = 'window.scrollTo(0, document.body.scrollHeight)'
	old_scroll_height = 0
	while((driver.execute_script(js1) > old_scroll_height) & (pageIndex < max_scrollPages)):
		old_scroll_height = driver.execute_script(js1)
		driver.execute_script(js2)
		pageIndex = pageIndex + 1
		time.sleep(3)

	content = driver.page_source
	driver.quit()
	return content

# select and store project source, with use of beautifulsoup
def get_projects(info):
	soup = BeautifulSoup(info, 'lxml')
	FindProjects = soup.find_all(class_="rf-project-cover")
	ProjectLinkList = []
	for projectdiv in FindProjects:
		project_title = str(projectdiv.contents[1].contents[1].get("title"))
		compact_title = ''.join(re.findall('[a-zA-Z0-9]+', project_title))
		project_url = projectdiv.contents[1].get("href")
		image_url = projectdiv.contents[1].contents[1].get("src")
		ProjectLinkList.append([compact_title, project_url, image_url])

	return ProjectLinkList

# save project info into xls
def writeExcel(data):
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Sheet1')
	ws.write(0, 0, 'Index')
	ws.write(0, 1, 'Project URL')
	ws.write(0, 2, 'Image URL')
	count = 1
	for item in data:
		for col in range(0, len(item)):
			ws.write(count, col, item[col])

		count = count + 1

	wb.save('projectURL.xls')

# --- end func definition
# --- scripts
socket.setdefaulttimeout(30)
# textile design is at field 95
url = 'https://www.behance.net/search?field=95&content=projects&sort=appreciations&time=week'
MAX_PAGE = 50
page_info = get_content(url, MAX_PAGE)
contents = get_projects(page_info)
writeExcel(contents)