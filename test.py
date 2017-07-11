from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='baca9285d9684ad9be61597e3fdc8f8a')

model = app.models.get('food-items-v1.0')

response = model.predict_by_url(url='https://www.mostluxuriouslist.com/wp-content/uploads/2015/11/Pizza.jpg')

print response

