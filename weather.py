import requests
url='https://tianqiapi.com/api'
parm={'appid':'65276869',
      'appsecret':'uHUxQHA2',
      'version':'v6',
      'city':'上海'}
respond=requests.get(url=url,params=parm)
m=respond.text
n=eval(m)
k=n["date"]
l=n["week"]
j=n["city"]
a=n['wea']
b=n['tem']
c=n['tem1']
d=n['tem2']
e=n['win']
f=n['air_level']
g=n['air_tips']
text='今天是:'+k+'，天气:'+a+'，最高温:'+c+'摄氏度，最低温:'+d+'摄氏度'+'\n'+'平均温度:'+b+'摄氏度,空气等级:'+f+',建议您:'+g+'今天也要努力加油哦!'
print(text)
print('---------------------------------------------------------------------------------')



