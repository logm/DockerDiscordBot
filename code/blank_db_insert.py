from tinydb import TinyDB, Query, where


db = TinyDB('db.json')




db.insert({
	'type': 'user',
	'userid': '',
	'discriminator': '',
	'username': '',
	'roles': [''],
	'lastOnlineDate': ''
	})
print("done")