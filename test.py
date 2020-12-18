#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import post_2_album
import album_sender
from telegram.ext import Updater

with open('token') as f:
	token = f.read().strip()
tele = Updater(token, use_context=True)
chat = tele.bot.get_chat(-1001198682178) # bot debug
# chat = tele.bot.get_chat('@web_record')

def test(url, rotate=False):
	result = post_2_album.get(url)
	print(result)
	# album_sender.send_v2(chat, result)
	
if __name__=='__main__':
	test('https://t.me/dushufenxiang/1355') # link