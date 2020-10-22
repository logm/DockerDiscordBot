import discord
from discord.ext import commands
import asyncio
import random
import datetime  # needed for logging information
import pytz
from roletable import userlist
from tinydb import TinyDB, Query, where
from secrets import secrets_token, secrets_botLogChannelID, secrets_admin_id

TOKEN = secrets_token
botLogChannelID = secrets_botLogChannelID

description = '''Starter discord bot using discord.py and docker-compose.'''

intents = discord.Intents.default()
# intents = discord.Intents(presences = True, members = True, messages = True)
intents.presences = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='?', intents=intents ,description=description)
db = TinyDB('db.json')
db.all()

@bot.event
# @asyncio.coroutine
async def on_ready():
	"""loads up when the bot inits"""
	print('Logged in as')
	print(bot.user.name)
	# print(bot.user.id)
	time = datetime.datetime.now().strftime("%b %d, %Y - %I:%M:%S")
	output = "Logging in " + time
	botLogChannel = bot.get_channel(botLogChannelID)
	await botLogChannel.send(output)
	f = open('log/login.log', 'a')
	f.write(output + '\n')
	f.close()
	print("bot is ready ")
	message = discord.Game("init")
	await bot.change_presence(status=discord.Status.idle, activity=message)
	bot.loop.create_task(bot.my_background_task(bot))
	print('------')


@bot.command()
async def sayinchannel(ctx, ch: int, msg):
	"""sends the message in desired channel"""
	channel = bot.get_channel(ch)
	await channel.send(msg)


@bot.event
async def on_message(message):
	if message.author.bot is False:
		output = message.created_at.now().strftime("%b %d, %Y - %I:%M:%S") + " #" + message.channel.name + " " + message.author.name + ": " + message.content
		# botLogChannel = bot.get_channel(botLogChannelID)
		# await botLogChannel.send(output)
		atmts = message.attachments
		for i in range(len(atmts)):
			attachment = atmts[i].url
			output = output + " ATTACHMENT: " + attachment
			fp = "log/files/" +	str(atmts[i].id) +"." + atmts[i].filename
			await atmts[i].save(fp)
		f = open('log/message.log', 'a')
		f.write(output + '\n')
		f.close()
	await bot.process_commands(message)


@bot.event
async def my_background_task(self):
	await self.wait_until_ready()
	while not self.is_closed():
		output = str(datetime.datetime.now().strftime("%a %I:%M"))
		message = discord.Game(output)
		await self.change_presence(status=discord.Status.idle, activity=message)
		# print(message)
		await asyncio.sleep(30)  # task runs every 30 seconds


@bot.event
async def on_member_update(before, after):
    # online = 'online'
    # offline = 'offline'
    # idle = 'idle'
    # dnd = 'dnd'
    # do_not_disturb = 'dnd'
    # invisible = 'invisible'
	# print("{} was {}.".format(before.name,before.status))
	# print("{} has gone {}.".format(after.name,after.status))
	userTable = db.search(where('type') == 'user')
	if (before.status != after.status):
		if (str(after.status) == "offline"):
			#remove roles
			username = after.name + "#" + after.discriminator
			for user in userTable:
				if (str(after.id) == str(user['userid'])):
					for role in user['roles']:
						newrole = discord.utils.get(before.guild.roles, name=role)
						await after.remove_roles(newrole)
			#add offline role
			# print("adding offline role")
			newrole = discord.utils.get(before.guild.roles, name="offline")
			await after.add_roles(newrole)
		else:
			#remove offline role
			# print("removing offline role")
			newrole = discord.utils.get(before.guild.roles, name="offline")
			await after.remove_roles(newrole)
			#add roles
			# print("adding roles")
			username = after.name + "#" + after.discriminator
			for user in userTable:
				if (str(after.id) == str(user['userid'])):
					for role in user['roles']:
						removedRole = discord.utils.get(before.guild.roles, name=role)
						await after.add_roles(removedRole)


@bot.command()
async def createRoleList(ctx):
	"""outputs list of users and their roles"""
	adminId = secrets_admin_id
	# print(ctx.message.author.id)
	if (str(ctx.message.author.id) == adminId):
		# print("user an admin")
		#Guild.members #is a list of Member
		memberList = ctx.message.guild.members
		for mem in memberList:
			if (mem.bot == False and mem.name != "Log"):
				# print(mem.id)
				roleList = []
				for role in mem.roles:
					# print(mem.name, role.name)
					if (role.name != "@everyone" and role.name != "offline"):
						roleList.append(role.name)
				db.insert({
					'type': 'user',
					'userid': str(mem.id),
					'discriminator': str(mem.name + "#" + mem.discriminator),
					'username': mem.display_name,
					'roles': roleList,
					'lastOnlineDate': ''
					})
				# print(str(roleList))
	else:
		print("user not an admin")
	db.all()


@bot.command()
async def addUser(ctx):
	"""outputs list of users and their roles"""
	adminId = secrets_admin_id
	# print(adminId)
	# print(ctx.message.author.id)
	if (str(ctx.message.author.id) == adminId):
		# print("user an admin")
		#Guild.members #is a list of Member
		memberList = ctx.message.guild.members
		for mem in memberList:
			if (mem.bot == False and mem.name != "Log"):
				# print(mem.id)
				roleList = []
				for role in mem.roles:
					# print(mem.name, role.name)
					if (role.name != "@everyone" and role.name != "offline"):
						roleList.append(role.name)
				db.insert({
					'type': 'user',
					'userid': str(mem.id),
					'discriminator': str(mem.name + "#" + mem.discriminator),
					'username': mem.display_name,
					'roles': roleList,
					'lastOnlineDate': ''
					})
				# print(str(roleList))
	else:
		print("user not an admin")
	db.all()

bot.run(TOKEN)
