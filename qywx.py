import requests
import  weather
from weather import *
def test_robot(message1):
    headers = {"Content-Type": "text/plain"}
    message = "上海市：{}".format({str(message1)})
    data = {
        "msgtype": "text",
        "text": {"content": message}
    }
    ret = requests.post(
        url="webhook",
        # 此处为新建机器人以后生成的链接
        headers=headers,
        json=data
    )
    print(ret.text)  # 成功后的打印结果：{"errcode":0,"errmsg":"ok"}
if __name__ == '__main__':
    test_robot(weather.text)