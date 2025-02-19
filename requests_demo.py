# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.jd.com/')

# 返回网页内容
print(x.text)
