import json
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time

def screen_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    headers = {
        "User-Agent": "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    province_list = requests.get(url, headers=headers, verify=True)
    province_dict = json.loads(province_list.text)
    province_dict_data = province_dict['data']
    province_dicts= json.loads(province_dict_data)
    province_dicts_data= province_dicts['areaTree'][0]['children']
    today_time = time.strftime("%Y-%m-%d")
    provinceList_data = []
    for i in range(len(province_dicts_data)):
        dict = {}
        dict['name'] = province_dicts_data[i]['name']
        dict['time'] = today_time
        dict['today_confirm'] = province_dicts_data[i]['today']['confirm']
        dict['total_confirm'] = province_dicts_data[i]['total']['confirm']
        dict['total_heal'] = province_dicts_data[i]['total']['heal']
        dict['total_dead'] = province_dicts_data[i]['total']['dead']
        provinceList_data.append(dict)
    return provinceList_data

def data_list():
    provinceList_name_list = []
    provinceList_today_confirm_list = []
    for i in screen_data():
        provinceList_name_list.append(i['name'])
        provinceList_today_confirm_list.append(i['today_confirm'])
    dic = dict(zip(provinceList_name_list,provinceList_today_confirm_list))
    return dic

def wc_data():
    wc_data = WordCloud(font_path = "./123.ttf",scale = 18,background_color = "white")
    wc_data.generate_from_frequencies(data_list())
    plt.imshow(wc_data)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    wc_data()













