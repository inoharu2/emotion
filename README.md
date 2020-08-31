# emotion

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 00:23:06 2020

@author: histu
"""


import requests
import json

image_path = r"C:\Users\histu\tello\test.jpg"
image =  open(image_path, 'rb').read()
url = "https://ai-api.userlocal.jp/face"
res = requests.post(url, files={"image_data": image})
data = json.loads(res.content)
result = data['result']
for r in result:
    print(f"""
    年齢: {r['age']}
    感情: {r['emotion']}
    感情内訳： {r['emotion_detail']}
    性別: {r['gender']}
    顔の向き: {r['head_pose']}
    顔の位置: {r['location']}
    """)
