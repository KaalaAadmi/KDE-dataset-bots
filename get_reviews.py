from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_titles(titles):
  l=[]
  for title in titles:
    x = title.replace(" ", "+")
    l.append(x)
  return l

def get_ids(url):
  val=url.split('/')
  return val[4]

ids=[]
titles=["The Dark Knight","The Dark Knight Rises","Black Adam"]
query_titles=get_titles(titles)
driver=webdriver.Chrome(executable_path=r"./chromedriver.exe")
# print(query_titles)
url="https://www.imdb.com/find?q="
for query_title in query_titles:
  url1=url+query_title
  driver.get(url1)
  sleep(3)
  try:
    element=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[1]').click()
  except:
    element=driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]').click()
  else:
    sleep(5)
    get_url = driver.current_url
    print(get_url)
    sleep(2)
    id=get_ids(get_url)
    print(id)
    ids.append(id)
driver.close()
print(ids)