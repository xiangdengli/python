import ddt
import requests
import time
import unittest

data_list=\
[{"dep_id":"HS2021","dep_name":"历史学院","master_name":"汪老师","slogan":"读史可以明智"},\
{"dep_id":"MKS2021","dep_name":"马克思学院","master_name":"马老师","slogan":"辩证思维"},\
{"dep_id":"PY2021","dep_name":"物理学院","master_name":"李老师","slogan":"多思考,多总结"},\
{"dep_id":"BIO2021","dep_name":"生物学院","master_name":"赵老师","slogan":"多实验"}]
@ddt.ddt()
class Post(unittest.TestCase):
    def setUp(self) -> None:
        self.url='http://127.0.0.1:8000/api/departments/'
        self.toubu={"content-Type":"application/json"}
    @ddt.data(*data_list)
    def test_post(self,dptinfo):
        shuju = r'{"data":[{"dep_id":"' +\
                   dptinfo["dep_id"]+\
                   r'","dep_name":"' +\
                   dptinfo["dep_name"]+\
                   r'","master_name":"' +\
                   dptinfo["master_name"]+\
                   r'","slogan":"' +\
                   dptinfo["slogan"]+ \
                   r'"}]}'
        jg5=requests.post(url=self.url,data=shuju.encode("utf-8"),headers=self.toubu)
        self.assertEqual(jg5.status_code,201)
        print(jg5.text)
    def tearDown(self) -> None:
        time.sleep(3)
if __name__=="__main__":
    unittest.main()