#!/usr/bin/env python

#coding: utf8


import irc

bot = irc.Client(
	nick='ExampleBot',
	password='NickServPASSWORD',
	ident='ErEnUa',
	realname='ErEnUa',
	host='irc.freenode.net',
	modules=['module_loader', 'general', 'ranks', 'ping', 'time', 'channel_main', 'channel_op', 'log_main', 'commands_basic']
)
bot.properties['autojoin'] = ['##erenua-bots']
bot.properties['prefix'] = '!'

bot.connect()
