import requests
import json 

def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulkV2'
    paramt={
        'authorization': '7RV0IhzXEmTSuYqFWJy63tMQ4vHB5nPeb9Ukg1jdDrK8GsL2oAvZc2pFK5lH0sJ8fj3dkSRrqmtN96ow',
        'sender_id': 'FSTSMS',
        'message': message,
        'numbers': number,
        'language': 'english',
        'route': 'q'    
    }

response=requests.get (url, paramt=paramt)

dic=response.json()
print(dic)

send_sms("7263987953", "This is my new message project")