import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'glucose':148  , 'bp':72, 'age':50})

print(r.json())
