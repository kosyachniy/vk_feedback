from func.vk import *
from dialogflow_feedback.main import answer
import time

while True:
	try:
		for i in read():
			req = answer(i[1])
			if not req: req = 'Не могу ответить на этот вопрос сразу! Опишите проблему подробнее:'
			send(i[0], req)
	except:
		pass

	time.sleep(0.1)