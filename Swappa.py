#!/usr/bin/python3.7

from bs4 import BeautifulSoup
import requests
import sendgrid
from sendgrid.helpers.mail import *

#SendGrid Credentials
sg = sendgrid.SendGridAPIClient(apikey='')
from_email = Email("test@example.com")
to_email = Email("text@example.com") #changeToEmail
subject = "Swappa Found"
content = Content("text/plain", "New Product Found at Swappa")
mail = Mail(from_email, subject, to_email, content)





price_list = []

hasReview= True

url='http://swappa.com/mobile/buy/apple-iphone-7/unlocked'
headers = {'user-agent': 'my-app/0.0.1'}
source= requests.get(url, headers=headers).text

url_parse= BeautifulSoup(source, 'lxml')



for content in url_parse.find_all('span', class_='price'):
    parse = content.text
    parse_split = parse.split('$')[1]
    price_list.append(parse_split)




for i in price_list:
	if int(i) < 250:
		response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)
		break