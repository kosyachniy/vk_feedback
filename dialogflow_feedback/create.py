# https://dialogflow.com/docs/reference/api-v2/rest/v2/projects.agent.intents/create

import requests
from enum import Enum

link = 'https://dialogflow.googleapis.com/v2/dialogflow.intents.create/intents'

params = {
	'languageCode': 'ru',
	# 'intentView': Enum(),
}

cont = {
	'name': '1.test',
	'displayName': '1.test',
	'webhookState': {'WebhookState': 'WEBHOOK_STATE_UNSPECIFIED'},
	# 'priority': number,
	# 'isFallback': boolean,
	# 'mlDisabled': boolean,
	# 'inputContextNames': [
	# 	string
	# ],
	# 'events': [
	# 	string
	# ],
	# 'trainingPhrases': [
	# 	{
	# 		object(TrainingPhrase)
	# 	}
	# ],
	# 'action': string,
	# 'outputContexts': [
	# 	{
	# 		object(Context)
	# 	}
	# ],
	# 'resetContexts': boolean,
	# 'parameters': [
	# 	{
	# 		object(Parameter)
	# 	}
	# ],
	# 'messages': [
	# 	{
	# 		object(Message)
	# 	}
	# ],
	# 'defaultResponsePlatforms': [
	# 	enum(Platform)
	# ],
	# 'rootFollowupIntentName': string,
	# 'parentFollowupIntentName': string,
	# 'followupIntentInfo': [
	# 	{
	# 		object(FollowupIntentInfo)
	# 	}
	# ],
}

cont = requests.post(link, params=params, json=cont)
print(cont.text)