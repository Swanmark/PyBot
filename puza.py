#-*- coding:utf-8 -*-
import socket
import time
import os
from random import randrange
import json


nick = "PuzaBot"
server = "irc.freenode.net"
ras = "#coinking"
nickservpass = "INSERT_PASSWORD_HERE"
bSize = "8192"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
time.sleep(1)
irc.recv(8192)
irc.send('NICK '+nick+'\r\n')
irc.send('USER PUZA PUZA PUZA :Puza is #1\r\n')
time.sleep(2)
irc.send('JOIN '+ras+'\r\n')
#irc.send('PRIVMSG nickserv :IDENTIFY DrPuza '+nickservpass+'\r\n')
while True:
  data = irc.recv(8192)
  print (data)
  if data.find('PING') != -1:
    irc.send('PONG ' +data.split()[1]+'\r\n')
  usrmsg = data.split(':')[-1].strip()
  firstmsg = usrmsg.split(' ')[0].lower()
  if firstmsg == "!love":
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0036► ► ► ► ► \0034LOVE ZONE\0036 ◄ ◄ ◄ ◄ ◄\r\n')
  if firstmsg == "!charity" or firstmsg == "!donate":
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :Donations to the following addresses will all go to charity! =D\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :Every month there will be a different charity recieving the donations.\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :BTC:  1A3k78jypUBPdBxroSBbGdhctNPttDo6FT\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :DOGE: DN1iT4njrHsb61FowPoHa2BQ49SozHw9ep\r\n')
    time.sleep(0.1)
    irc.send('PRIVMSG '+chan+' :LTC:  LMWYxZ2jbKhkYqU1jWo2LPUY3Wy255o2nu\r\n')
  time.sleep(0.01)
