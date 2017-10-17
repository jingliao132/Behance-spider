# Behance-spider
Crawl images from Behance.net, field of textile design as example<br>
Retrieve project URLs and save as xls

## Pre-requirements
1. Install ButterSoup4 and selenium<br>
`pip install BeautifulSoup4`<br>
`pip install selenium`<br>
2. Install support packages of regular expression, excel and socket connection<br>
`pip install re`<br>
`pip install xlwt`<br>
`pip install socket`<br>
3. Install browser webdriver<br>
Download and install from browser support page

## Steps
1. Run RetrieveProject.py<br> 
THis will grasp project urls from Behance.net, and save in file ProjectURL.xls<br>
A pre-generated ProjectURL.xls is provided.<br>

2. Run RetrieveImages.py<br>
This will download images of each project in ProjectURL.xls, and save in fold 'pic1' under the root<br>
Downloading process and infomation will be printed
