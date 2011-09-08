#!/usr/bin/env python

#coding: utf8


import irc

bot = irc.Client(
	nick='iForceBot',
	password='superword',
	ident='iForceBot',
	realname='iForceBot by Daniel Bugl (Daniel0108)',
	host='irc.wiseeyes.co.cc',
	modules=['module_loader', 'general', 'ranks', 'ping', 'time', 'channel_main', 'log_main', 'quit', 'channel_op', 'commands_basic', 'downloader']
)
bot.properties['autojoin'] = ['#iforcebot']
bot.properties['prefix'] = '?'

bot.connect()
