
###!/usr/bin/env python

#coding: utf8


import handler

class Enable(handler.Handler): # Change to your module's name
        def privmsg(self, words):
                line = ' '.join(words)
                msg = line.split(':')[2]
                msg_words = msg.split(' ')
                nick = line.split(':')[1].split('!')[0]
                target = words[2]
		module_downloader_server = self.commands.getvar('module_downloader_server')

                if target.find('#') != 0:
                        target = nick
                if len(msg_words) >= 1:
			if self.commands.getcmd(msg_words[0], 'enable') and self.commands.getrank(nick) == 7:
				if msg_words[1] == 'register':
					self.commands.setvar('registration_enabled', 'True')
					self.commands.notice(nick, "Registration enabled.")
				elif msg_words[1] == 'login':
					self.commands.setvar('login_enabled', 'True')
					self.commands.notice(nick, "Login enabled.")
				elif msg_words[1] == 'downloader':
					self.commands.setvar('module_downloader_enabled', 'True')
					self.commands.notice(nick, "Module Downloader enabled.")
					self.commands.notice(nick, "The module downloader server is currently set at %s." % module_downloader_server)
			elif self.commands.getcmd(msg_words[0], 'disable'):
                                if msg_words[1] == 'register':
                                        self.commands.setvar('registration_enabled', False)
                                        self.commands.notice(nick, "Registration disabled.")
                                elif msg_words[1] == 'login':
                                        self.commands.setvar('login_enabled', 'True')
                                        self.commands.notice(nick, "Login disabled.")
                                elif msg_words[1] == 'downloader':
                                        self.commands.setvar('module_downloader_enabled', 'True')
                                        self.commands.notice(nick, "Module Downloader disabled.")
