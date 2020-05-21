import requests

# url = 'https://api.githup.com/search/repositories?q=language:python&sort=stars'
url = "https://www.baidu.com/"
r = requests.get(url)
print('Status code:',r.status_code)