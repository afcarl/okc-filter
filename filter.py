import sys
import unicodedata
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter


class OkcSession(object):
	def __init__(self, username, password):
		self.session = requests.Session()
		credentials = {'username': username, 'password': password, 'dest': '/'}
		resp = self.session.post('https://www.okcupid.com/login', data=credentials)
		self.message_threads = None

	def get_message_threads(self, force_reload=False):
		if self.message_threads is None or force_reload:
			html_doc = self.session.get('http://www.okcupid.com/messages').content
			soup = BeautifulSoup(html_doc)
			msg_divs = soup.find(id='messages').find_all('li')
			self.message_threads = [self.extract_message_thread(m) for m in msg_divs]
		return self.message_threads

	def extract_message_thread(self, div):
		thread_id = div['id'][8:]
		from_user = div.find(class_='subject').text
		unread = 'unreadMessage' in div['class']
		return OkcMessageThread(self.session, thread_id, from_user, unread)

class OkcMessageThread(object):
	def __init__(self, session, thread_id, from_user, unread=False):
		self.session = session
		self.thread_id = thread_id
		self.from_user = from_user
		self.unread = unread
		self.messages = None
		self.read_msg_url = 'http://www.okcupid.com/messages?readmsg=true&threadid={0}&folder=1'.format(thread_id)
		self.delete_url = 'http://www.okcupid.com/mailbox?ajax=1&deletethread=1&deletemsg=0&threadid={0}&msgid=0'.format(thread_id)

	def get_messages(self, force_reload=False):
		if self.messages is None or force_reload:
			html = self.session.get(self.read_msg_url).content
			self.messages = self.extract_all_messages(html)
		return self.messages

	def extract_all_messages(self, html_doc):
		soup = BeautifulSoup(html_doc)
		msg_divs = soup.find(id='thread').find_all('li')
		messages = [self.extract_message(m) for m in msg_divs if m['id'] != 'collapse' and \
																		m['id'] != 'new_msg' and \
																		m['id'] != 'compose']
		return messages

	def extract_message(self, div):
		msg_id = div['id'][8:]
		text = div.find(class_='message_body', recursive=True).text
		text = unicodedata.normalize('NFKD', text).encode('ascii','ignore').strip()
		timestamp = div.find(class_='fancydate', recursive=True).text
		timestamp = unicodedata.normalize('NFKD', timestamp).encode('ascii','ignore')
		from_me = 'from_me' in div['class']
		return OkcMessage(msg_id, self.from_user, text, timestamp, from_me)

	def delete(self):
		try:
			self.session.get(self.delete_url)
		except:
			return False
		return True

class OkcMessage(object):
	def __init__(self, msg_id, user, text, timestamp, from_me=False):
		self.msg_id = msg_id
		self.user = user
		self.text = text
		self.timestamp = timestamp
		self.from_me = from_me

class OkcMessageFilter(object):
	def __init__(self, session, keywords):
		self.session = session
		self.keywords = keywords
		self.pattern = '(\W+|^)({0})(\W+|$)'.format('|'.join(map(re.escape, keywords)))

	def apply_filter(self, skip_read=True):
		threads = okc.get_message_threads(force_reload=True)
		for thread in threads:
			if skip_read and thread is not unread:
				continue
			for message in thread.get_messages():
				scan_results = re.findall(self.pattern, message.text, re.IGNORECASE)
				if len(scan_results) > 0:
					print 'Message from {0}: FOUND KEYWORD(s): ({1})'.format(thread.from_user, [x[1] for x in scan_results])
				else:
					print 'Message clean: {0}'.format(message.text)


if __name__ == '__main__':
	username = sys.argv[1]
	password = sys.argv[2]
	with open('keywords.txt', 'rb') as keywords_file:
		keywords = [word.strip() for word in keywords_file if len(word.strip()) > 0 and not word.strip().startswith('#')]
	print 'Keywords: {0}'.format(keywords)
	okc = OkcSession(username, password)
	msg_filter = OkcMessageFilter(okc, keywords)
	msg_filter.apply_filter(skip_read=False)
