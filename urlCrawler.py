import re
import requests

web =  raw_input("Url: ")

response = requests.get('http://'+web).text

urls = []

pattern= re.compile('''href=["'](.[^"']+)["']''')
search = re.findall(pattern, response)

for url in search:
	 try:
		  urls.append(url)
		  d1 =  str(url)
		  urlList = open('crawler_url.txt','a+')
		  urlList.write(d1+"\n")
		  urlList.close()
		  print url
		  response2 = requests.get(i).text
		  search2 = re.findall(pattern, response2)
		  for e in search2:
			   urls.append(e)
			   d2 =  str(e)
			   urlList = open('crawler_url.txt','a+')
			   urlList.write(d2+"\n")
			   urlList.close()
			   
	 except Exception,e:
		  pass
	
print "URls saved in file urlCrawler.txt"