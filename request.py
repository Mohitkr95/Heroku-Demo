import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'NewYork':1, 'California':0, 'Florida':0, 
                            'test_score':165349.2, 'interview_score':136897.8, 'interview_scor': 471784.1})

print(r.json())