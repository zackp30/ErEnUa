#!/usr/bin/env python

#coding: utf8


import handler


class Setup(handler.Handler):
	def privmsg(self, words):
		line = ' '.join(words)
		msg = line.split(':')[2]
		msg_words = msg.split(' ')
		nick = line.split(':')[1].split('!')[0]
		target = words[2]

		if target.find('#') != 0:
			target = nick
		
		if self.commands.getvar('setup_run') == 'True':
			print "ERR: Setup already run. Not running bot setup."
			self.client.unload_module('setup')
		elif self.commands.getvar('setup_run') != 'True':
			if self.commands.getcmd(msg_words[0], 'setup') and self.commands.getrank(nick) == 7:
				if self.commands.getvar('language') != 'en':
					self.commands.setvar('language', 'en')
					print "Language set to 'en' (English)"
				if self.commands.getvar('registration_enabled') != 'True':
					self.commands.setvar('registration_enabled', 'True')
					print "Enabling registration."
				if self.commands.getvar('login_enabled') != 'True':
					self.commands.setvar('login_enabled', 'True')
					print "Enabling logins."
				if self.commands.getvar('module_downloader_enabled') != 'True':
					self.commands.setvar('module_downloader_enabled', 'True')
					self.commands.setvar('module_downloader_server', 'www.wiseeyes.co.cc')
				print "Setup complete."
				self.commands.notice(nick, "Bot setup complete. To enable or disable registration and logins, use %senable/%sdisable login/register or %sunload register." % (self.client.properties.get('prefix'), self.client.properties.get('prefix'), self.client.properties.get('prefix')))
				self.commands.setvar('setup_run', 'True')
				self.client.unload_module('setup')
