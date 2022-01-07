import requests
import time
from bs4 import BeautifulSoup


link = open('link.txt','r',encoding='utf-8').read().splitlines()
for url in link:
 
    
    # Gửi 1 request đến url phía trên và nhận lại source page của nó
    r = requests.get(url)
   
    
    
    # Làm đẹp source 
    # Mình dùng lxml parser cho nhanh, 
    # Ngoài ra có html.parser, lxml-xml, html5lib (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    soup = BeautifulSoup(r.content, 'lxml')
    
   
    # Lấy thẻ tiêu đề bài báo
    #print(soup.title)
    # Lấy nội dung tiêu đề
    #print(soup.title.text)
    if soup.title.text == 'Zalo App':
        print('Link Hỏng '+url)
    else:
        print(soup.title.text)