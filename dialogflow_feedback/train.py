import apiai, json

with open('keys.json', 'r') as file:
	token_dialogflow = json.loads(file.read())['token_dialogflow']

request = apiai.ApiAI(token_dialogflow).user_entities_request('faq.1.10655')

print(request.send())
print(dir(request))