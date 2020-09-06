# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:03:56 2020

@author: histu
"""


import cv2
import os
import datetime
import requests
import json

#カメラ画像取得
def save_frame_camera_cycle(device_num, dir_path, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        if n == cycle:
            n = 0
            #ver1
            #cv2.imwrite('{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), ext), frame)
            
            #ver2
            image_path = '{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), ext)
            cv2.imwrite(image_path, frame)


            #表情解析#############################################
            
            #ver1
            #image_path = r"C:\Users\histu\tello\test.jpg"
            
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
            ######################################################
        n += 1
        
    cv2.destroyWindow(window_name)


save_frame_camera_cycle(0, r"C:\Users\histu\tello", 'camera_capture_cycle', 300)
#30 = 1秒

