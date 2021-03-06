import requests, time, json
from bs4 import BeautifulSoup

def load_cat(id, add=''):
	url = 'https://vk.com/support?act=faqs' + add + '&c=' + str(id)
	page = requests.get(url).text
	soup = BeautifulSoup(page, 'html5lib') #'lxml')

	reqs = []

	cat = soup.find('h3', {'id': 'help_table_questions__title'}).text.strip()
	print(cat)

	table = soup.find('div', {'id': 'help_table_questions_l'})
	tr = table.find_all('div', {'class': 'help_table_question'})
	for que_id, i in enumerate(tr):
		que = i.find('a', {'class': 'help_table_question__q'}).text.strip()
		ans = i.find('div', {'class': 'help_table_question__ans'}).text.strip()
		#print(que, ans)

		reqs.append([cat, que, ans, que_id])

	return reqs

list_cat = ('', '_api')

with open('answers.json', 'w') as file:
	for u in list_cat:
		url = 'https://vk.com/support?act=home' + u
		page = requests.get(url).text
		soup = BeautifulSoup(page, 'html5lib') #'lxml')

		cats = soup.find_all('a', {'class': 'help_tile__title_a'})
		for i in cats:
			cat_id = i['href'].split('=')[-1]

			for j in load_cat(cat_id, u):
				req = json.dumps({'question': j[1], 'answer': j[2], 'section': 'home' + u, 'category': j[0], 'category_id': cat_id, 'id': j[3]}, ensure_ascii=False)
				print(req, file=file)

			time.sleep(1)