class Person:
	def __init__(self, name, roles):
		self.name = name
		self.userRoles = roles
	def getName(self):
		return  self.name
	def addRoles(self, role):
		self.userRoles.append(role)
	def getRoles(self):
		for i in self.userRoles:
			# print(i)
			return self.userRoles
	def getNumberOfRoles(self):
		return len(self.userRoles)
	def getRoleAt(self, num):
		return self.userRoles[num]


userlist = []
userlist.append(Person("Armin#2559", ["Gamers", "succbois"]))
userlist.append(Person("FairestSnake64#8606", ["people"]))
userlist.append(Person("Ferg#3481", ["people"]))
userlist.append(Person("Ghilliemania#7916", ["Gamers"]))
userlist.append(Person("GillOrBeGilled#7025", ["peeps"]))
userlist.append(Person("Greenytre#7550", ["Gamers", "Plebs", "succbois"]))
userlist.append(Person("JonyTones#5938", ["Gamers"]))
userlist.append(Person("Kaikyoin#7501", ["people"]))
userlist.append(Person("Lking75#5383", ["people"]))
userlist.append(Person("MartyQ#5244", ["Gamers"]))
userlist.append(Person("Moromanlml#8176", ["Gamers"]))
userlist.append(Person("Nick#9292", ["Gamers", "peeps"]))
userlist.append(Person("Philly#4082", ["Plebs", "Gamers"]))
userlist.append(Person("REEEEE#4418", ["Gamers"]))
userlist.append(Person("RecklessFaith#9471", ["Gamers", "peeps"]))
userlist.append(Person("Ryan Goosling#1396", ["Gamers", "succbois", "Queen"]))
userlist.append(Person("SPACECOW#4380", ["Gamers"]))
userlist.append(Person("Sensei#3405", ["people"]))
userlist.append(Person("shrimpidiot#5242", ["Gamers", "Plebs", ]))
userlist.append(Person("Silvr90210#9479", ["Gamers", "peeps"]))
userlist.append(Person("Skulleez#5269", ["peeps"]))
userlist.append(Person("StealthyNinja#3199", ["Gamers"]))
userlist.append(Person("The Hotstepper#8578", ["Gamers", "peeps"]))
userlist.append(Person("TheOvenIsOnFire#3814", ["people"]))
userlist.append(Person("Tornado#4213", ["Gamers", "peeps"]))
userlist.append(Person("KingKaZR#5327", ["Gamers", "peeps"]))
userlist.append(Person("willl#3251", ["Gamers", "people"]))
userlist.append(Person("Gam69#1897", ["Gamers"]))
userlist.append(Person("Chutch#1290", ["Gamers"]))
userlist.append(Person("HudBear#5372", ["Gamers"]))
userlist.append(Person("MasatoMonkey#1160", ["Gamers"]))
userlist.append(Person("Sw1fty#5495", ["Gamers"]))
userlist.append(Person("Hash_Hamilton#5377", ["Gamers"]))
userlist.append(Person("несаллы#0445", ["people"]))



# from tinydb import TinyDB, Query


# db = TinyDB('db.json')

# db.purge()
# db.all()



# db.insert({
# 	'type': 'user',
# 	'userid': '187625932746391552',
# 	'discriminator': 'Armin#2559',
# 	'username': '',
# 	'roles': ['Gamers', 'succbois'],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '130923626089283584',
# 	'discriminator': 'FairestSnake64#8606',
# 	'username': '',
# 	'roles': ['people'],
# 	'lastOnlineDate': ''
# 	})

# db.insert({
# 	'type': 'user',
# 	'userid': '198254786565505025',
# 	'discriminator': 'Ferg#3481',
# 	'username': '',
# 	'roles': ['people'],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '230100303620341760',
# 	'discriminator': 'Ghilliemania#7916',
# 	'username': '',
# 	'roles': ['Gamers'],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '214560486258245633',
# 	'discriminator': 'GillOrBeGilled#7025',
# 	'username': '',
# 	'roles': ['peeps'],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '258115195325382656',
# 	'discriminator': 'Greenytre#7550',
# 	'username': '',
# 	'roles': ["Gamers", "Plebs", "succbois"],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '128948243311755265x',
# 	'discriminator': 'JonyTones#5938',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '',
# 	'discriminator': 'Kaikyoin#7501',
# 	'username': '',
# 	'roles': ["people"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '336665712192126988',
# 	'discriminator': 'Lking75#5383',
# 	'username': '',
# 	'roles': ["people"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '',
# 	'discriminator': 'MartyQ#5244',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '281278009229705216',
# 	'discriminator': 'Moromanlml#8176',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '185950311029014528',
# 	'discriminator': 'Nick#9292',
# 	'username': '',
# 	'roles': ["Gamers", "peeps"],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': 'x',
# 	'discriminator': 'Philly#4082',
# 	'username': '',
# 	'roles': ["Plebs", "Gamers"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': 'x',
# 	'discriminator': 'REEEEE#4418',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '145690713865191426',
# 	'discriminator': 'RecklessFaith#9471',
# 	'username': '',
# 	'roles': ["Gamers", "peeps"],
# 	'lastOnlineDate': ''
# 	})




# db.insert({
# 	'type': 'user',
# 	'userid': '185929422300381184',
# 	'discriminator': 'Ryan Goosling#1396',
# 	'username': '',
# 	'roles': ["Gamers", "succbois", "Queen"],
# 	'lastOnlineDate': ''
# 	})




# db.insert({
# 	'type': 'user',
# 	'userid': 'x',
# 	'discriminator': 'x',
# 	'username': '',
# 	'roles': ['x'],
# 	'lastOnlineDate': ''
# 	})




# db.insert({
# 	'type': 'user',
# 	'userid': '502347916317556757',
# 	'discriminator': 'SPACECOW#4380',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})







# db.insert({
# 	'type': 'user',
# 	'userid': '212408639024136193',
# 	'discriminator': 'shrimpidiot#5242',
# 	'username': '',
# 	'roles': ["Gamers", "Plebs", ],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '225044229787746304',
# 	'discriminator': 'Silvr90210#9479',
# 	'username': '',
# 	'roles': ["Gamers", "peeps"],
# 	'lastOnlineDate': ''
# 	})



# db.insert({
# 	'type': 'user',
# 	'userid': '263832144588046336',
# 	'discriminator': 'Skulleez#5269',
# 	'username': '',
# 	'roles': ["peeps"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '562481339459305503',
# 	'discriminator': 'StealthyNinja#3199',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '188182268332736512',
# 	'discriminator': 'The Hotstepper#8578',
# 	'username': '',
# 	'roles': ["Gamers", "peeps"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '214558031243902979',
# 	'discriminator': 'TheOvenIsOnFire#3814',
# 	'username': '',
# 	'roles': ["people"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '311908858853326850',
# 	'discriminator': 'Tornado#4213',
# 	'username': '',
# 	'roles': ["Gamers", "peeps"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '205561917660594177',
# 	'discriminator': 'KingKaZR#5327',
# 	'username': '',
# 	'roles': ["Gamers", "peeps"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': 'x',
# 	'discriminator': 'willl#3251',
# 	'username': '',
# 	'roles': ["Gamers", "people"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '272256128803536896',
# 	'discriminator': 'Gam69#1897',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})


# db.insert({
# 	'type': 'user',
# 	'userid': '382368686117355523',
# 	'discriminator': 'Chutch#1290',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})

# db.insert({
# 	'type': 'user',
# 	'userid': '335556670912462848',
# 	'discriminator': 'Sw1fty#5495',
# 	'username': '',
# 	'roles': ["Gamers"],
# 	'lastOnlineDate': ''
# 	})



# db.all()

# for item in db:
# 	print(item)
