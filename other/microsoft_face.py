import requests
import json

# 微軟金鑰
subscription_key = 'aa56608b4ded4383830596cd9c087eb2'

# 斷言，若變數未定義強制引發錯誤
assert subscription_key

# 臉部辨識API網址
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

# 圖片網址
image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# API參數
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

# API回傳值
response = requests.post(face_api_url, params = params, headers = headers, json = {"url": image_url})
print(json.dumps(response.json()))