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
This script will grasp project urls from Behance.net, and save in file ProjectURL.xls<br>
A pre-generated ProjectURL.xls is provided.<br>

2. Run RetrieveImages.py<br>
This script will download images of each project in ProjectURL.xls, and save in fold 'pic1' under the root<br>
Downloading process and infomation will be printed.<br>
If fail to download a image from the url, 0 will be writen at the corresponding row in ProjectURL.xls. Else, 1 will be written.

3. Run TransformImages.py<br>
This script will convert different images to JPEG file with RGB colorspace.
