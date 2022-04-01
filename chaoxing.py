import requests
import re
import time
import datetime
headers={
		"User-agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	}
today = datetime.datetime.now()
nowtime=today.strftime('%Y-%m-%d')
lasttime=(today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
url="http://office.chaoxing.com/front/web/apps/reservepc/item?itemId=9087&reserveId=2656&fidEnc=bb3acc50f157286e"
session=requests.session()
login_api = "https://passport2.chaoxing.com/api/login"
params = {
            "name": "17683833838",
            "pwd": "wxl59420",
            "verify": "0",
            "schoolid":  ""
        }
resp = session.get(login_api, params=params,headers=headers)
r1=session.post(url=url,headers=headers).text
tokenlist= re.findall(r'token:(.*)\r', r1)
token=tokenlist[0]
token1=token.replace("'","")
token2=token1.strip()
time_text=session.get("http://office.chaoxing.com/data/apps/reserve/item/detail?id=9087",headers=headers).text
obj =re.compile(r'"\d{1,2}:\d{1,2}\\"', re.S)
times=obj.finditer(time_text)
print(type(time))
print("预约时间表")
for li in times:
    print(li.group().strip('"\\"'))
timeurl="https://office.chaoxing.com/data/apps/reserve/item/user/list?itemId=9087&startTime="+nowtime+"&endTime="+lasttime
time_data=session.get(url=timeurl,headers=headers).text
print(time_data)
a=input("请输入开始预约时间")
b=input("请输入结束预约时间")
start=nowtime+" "+a
end=nowtime+" "+b
data={
        "itemId":"9087",
        "reserveId":"2656",
        "date":nowtime,
        "startTime":start,
        "endTime":end,
        "remark":"",
        "intervalIdStr":"724586",
        "token":token2,
}
r2=session.post("http://office.chaoxing.com/data/apps/reserve/submit/reserve",headers=headers,data=data).text
if r2 =='{"success":true}':
    print("预约成功！")
else:
    print("预约失败！")


