import requests
import fake_useragent
from bs4 import BeautifulSoup


user = fake_useragent.UserAgent().random

header = {'user-agent': user}

link = "https://browser-info.ru/"
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id="tool_padding")

""" Check JS """
check_js = block.find('div', id="javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript:{status_js}'

""" Check Flash """
ckeck_flash = block.find('div', id="flash_version")
status_flash = ckeck_flash.find_all('span')[1].text
result_flash = f'Flash: {status_flash}'


""" Check User-Agent """
check_user_agent = block.find('div', id="user_agent").text

print(check_user_agent)
print(result_flash)
print(result_js)


""" If i want to parse the link """
""" find(a).get("href") """
