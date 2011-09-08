#!/usr/bin/env python

#coding: utf8


import irc

bot = irc.Client(
	nick='ErEnUa',
	password='superword',
	ident='ErEnUa',
	realname='ErEnUa Bot - Based off iForceBot',
	host='irc.freenode.net',
	modules=['module_loader', 'general', 'ranks', 'ping', 'time', 'channel_main', 'log_main', 'quit', 'channel_op', 'commands_basic']
)
bot.properties['autojoin'] = ['#ErENua', '#erenua-bots', '##eyesismine']
bot.properties['prefix'] = '?'

bot.connect()
