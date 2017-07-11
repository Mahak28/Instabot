import requests

BASE_URL = 'https://apis.paralleldots.com/'
API_KEY ='UXqiW0EEfpWD1oB8AgJXAveneCAQxkIQSGXZwbAioS0'

input = raw_input('Enter text:')
request_url = BASE_URL + 'sentiment?sentence1=%s&apikey=%s' %(input,API_KEY)
#request_url = 'https://apis.paralleldots.com/sentiment?sentence1=sachin%20is%20the%20best%20cricketer&apikey=UXqiW0EEfpWD1oB8AgJXAveneCAQxkIQSGXZwbAioS0'
response = requests.get(request_url, verify=False).json()
print response
