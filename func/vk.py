# Урезанный модуль из моего репозитория: https://github.com/kosyachniy/dev/tree/master/bot/vk/func

import time, requests, vk_api, json

with open('keys.json', 'r') as file:
	s=json.loads(file.read())
	vk=vk_api.VkApi(token=s['token_vk'])

def send(user, cont):
	return vk.method('messages.send', {'user_id':user, 'message':cont})

read = lambda: [[i['user_id'], i['body'], i['attachments'] if 'attachments' in i else []] for i in vk.method('messages.get')['items'] if not i['read_state']][::-1]

dial = lambda: [i['message']['user_id'] for i in vk.method('messages.getDialogs')['items']]