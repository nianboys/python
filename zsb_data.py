import requests
import json
class zsb:
    def __init__(self,phone,password):
        self.phone=phone
        self.password=password

    def screen_token(self):
        headers={
            "Authorization": "Basic Y2xpZW50LTAxOmNsaWVudC0wMS1zZWNyZXQ=",
            "Connection": "keep-alive",
            "Host": "zsb.e21.cn",
            "Referer": "https://zsb.e21.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }
        data={
            "scope": "all",
            "grant_type": "password",
            "username": self.phone,
            "password": self.password,
        }
        login_url="https://zsb.e21.cn/oauth/token"
        index_text=requests.post(url=login_url,headers=headers,data=data).text
        zsb_dict = json.loads(index_text)
        self.acess_token=zsb_dict['data']["access_token"]

    def screen_data(self):
        url = "https://zsb.e21.cn/api/v1/statistics/applyNum?total=0&_page=1&_limit=700&universityId=&majorId=&applyRate="
        headers = {
            "Authorization": "Bearer "+self.acess_token,
            "Connection": "keep-alive",
            "Host": "zsb.e21.cn",
            "Referer": "https://zsb.e21.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }
        page_text=requests.get(url=url,headers=headers).text
        zsb_dict=json.loads(page_text)
        zsb_dicts=zsb_dict['data']['records']

        zsb_data=[]
        for i in range(len(zsb_dicts)):
            dict={}
            dict['majorName']=zsb_dicts[i]['majorName']
            dict['number']=zsb_dicts[i]['number']
            dict['universityName']=zsb_dicts[i]['universityName']
            dict['count']=zsb_dicts[i]['count']
            zsb_data.append(dict)
        zsb_datas=[]
        for i in zsb_data:
            if not i in zsb_datas:
                zsb_datas.append(i)
        print(zsb_datas)

if __name__ == '__main__':
    run = zsb("","")
    run.screen_token()
    run.screen_data()

