# https://dialogflow.com/docs/reference/agent/intents

import requests, json

with open('keys.json', 'r') as file:
	developer_token_dialogflow = json.loads(file.read())['developer_token_dialogflow']

link = 'https://api.dialogflow.com/v1/intents?v=20150910'

headers = {
	'Authorization': 'Bearer ' + developer_token_dialogflow,
	'Content-Type': 'application/json',
}

def add(intent):
	print(intent['question'])

	cont = {
		'contexts': [],
		'events': [],
		'fallbackIntent': False,
		'name': 'faq.%s.%s.%d' % (intent['section'], intent['category_id'], intent['id']),
		'priority': 500000,
		'responses': [
			{
				'action': 'add.list',
				'affectedContexts': [],
				'parameters': [],
				'defaultResponsePlatforms': {},
				'messages': [
					{
						'speech': intent['answer'],
						'type': 0,
					}
				],
				'resetContexts': False,
			}
		],
		'userSays': [{
			'data': [{
				'text': intent['question'],
        	}],
			'isTemplate': False,
			'isAuto': False,
		}],
		'templates': [],
		'webhookForSlotFilling': False,
		'webhookUsed': False,
	}

	requests.post(link, headers=headers, json=cont)

with open('answers.json', 'r') as file:
	for i in file:
		add(json.loads(i))

# cont = {
# 	'contexts': [
# 		'shop'
# 	],
# 	'events': [],
# 	'fallbackIntent': False,
# 	'name': 'add-to-list',
# 	'priority': 500000,
# 	'responses': [
# 		{
# 			'action': 'add.list',
# 			'affectedContexts': [
# 				{
# 					'lifespan': 5,
# 					'name': 'shop',
# 					'parameters': {}
# 				},
# 				{
# 					'lifespan': 5,
# 					'name': 'chosen-fruit',
# 					'parameters': {}
# 				}
# 			],
# 			'defaultResponsePlatforms': {
# 				'google': True
# 			},
# 			'messages': [
# 				{
# 					'platform': 'google',
# 					'textToSpeech': 'Okay. How many $fruit?',
# 					'type': 'simple_response'
# 				},
# 				{
# 					'speech': 'Okay how many $fruit?',
# 					'type': 0
# 				}
# 			],
# 			'parameters': [
# 				{
# 					'dataType': '@fruit',
# 					'isList': True,
# 					'name': 'fruit',
# 					'prompts': [
# 						'I didn\'t get that. What fruit did you want?'
# 					],
# 					'required': True,
# 					'value': '$fruit'
# 				}
# 			],
# 			'resetContexts': False
# 		}
# 	],
# 	'templates': [
# 		'@fruit:fruit ',
# 		'Add @fruit:fruit ',
# 		'I need @fruit:fruit '
# 	],
# 	'userSays': [
# 		{
# 			'count': 0,
# 			'data': [
# 				{
# 					'alias': 'fruit',
# 					'meta': '@fruit',
# 					'text': 'oranges',
# 					'userDefined': True
# 				}
# 			]
# 		},
# 		{
# 			'count': 0,
# 			'data': [
# 				{
# 					'text': 'Add '
# 				},
# 				{
# 					'alias': 'fruit',
# 					'meta': '@fruit',
# 					'text': 'bananas',
# 					'userDefined': True
# 				}
# 			]
# 		},
# 		{
# 			'count': 0,
# 			'data': [
# 				{
# 					'text': 'I need '
# 				},
# 				{
# 					'alias': 'fruit',
# 					'meta': '@fruit',
# 					'text': 'apples',
# 					'userDefined': True
# 				}
# 			]
# 		}
# 	],
# 	'webhookForSlotFilling': False,
# 	'webhookUsed': False,
# }