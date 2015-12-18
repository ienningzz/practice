import bs4,requests,re
def get_messages(im):
	message = bs4.BeautifulSoup(im.content,'html.parser')
	mg = message.find(id="item_detail")
	print mg.text
	num = mg.find_all('dd')[2].text.encode('utf-8')
	number = re.match(r'(\d+)(\W?)(\d+)(\W?)(\d+)(\W?)(\d+)(\W?)(\d+)',num).group().split('-')
	end = ''.join(number)
	address = requests.get('http://210.35.251.243/opac/ajax_douban.php?isbn=' + end)
	print eval(address.content)['summary'].decode('unicode-escape')
def match(name):
	response = requests.get('http://210.35.251.243/opac/ajax_top_lend_shelf.php')
	soup = bs4.BeautifulSoup(response.content,'html.parser')
	sou = soup.find(id="search_container_center")
	for i in sou.find_all('a'):
		if name == i.text:
			im = requests.get(('http://210.35.251.243/opac/' + i['href']))
			break
		else:
			pass
	return get_messages(im)
def main():
	s = raw_input("Write your book name: ")
	match(s)
if __name__ == '__main__':
	main()
