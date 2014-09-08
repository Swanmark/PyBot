#-*- coding:utf-8 -*-
import socket
import time
import os
from random import randrange
import urllib2
import ssl
import hashlib
import random
from time import strftime

nick = "bot1337"
server = "rekt.club"
ras = "#irc"

s0cket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc = ssl.wrap_socket(s0cket)
irc.connect((server, 31337))

irc.write('PASS swanmark:asdf123\r\nNICK '+nick+'\r\nUSER 1 2 3 :4\r\n')

time.sleep(1)
irc.recv(8192)
time.sleep(1)
irc.send('JOIN '+ras+'\r\n')
seenenabled = "false"
rektenabled = "false"
while True:
  data = irc.recv(8192)
  print (data)
  usrmsg = data.split(':')[-1].strip()
  firstmsg = usrmsg.split(' ')[0].lower()
  try:
    firstmsgmc = usrmsg.split(' ')[1].lower()
  except:
    firstmsgmc = "error"
  if data.find('PING') != -1:
    irc.send('PONG ' +data.split()[1]+'\r\n')
  if data.lower().find('rekt') != -1 and rektenabled == "true":
    chan = data.lower().split()[2]
    nick = data.lower().split('!')[0].replace(':', '').strip()
    print nick
    if chan == "#gussi.is":
      if nick != "swanmark":
        irc.send('PRIVMSG '+chan+' :[X] Rekt [ ] Not rekt\r\n')
### TROLLSTUFF
###
### YOLO
  if firstmsg == "!enable":
    chan = "#gussi.is"
    try:
      arg1 = usrmsg.split()[1].lower()
    except:
      arg1 = "error"
    if arg1 != "error":
      if arg1 == "seen":
        seenenabled = "true"
        irc.send('PRIVMSG '+chan+' :'+arg1.title()+' enabled succesfully.\r\n')
      elif arg1 == "rekt":
        rektenabled = "true"
        irc.send('PRIVMSG '+chan+' :'+arg1.title()+' enabled successfully.\r\n')
      else:
        irc.send('PRIVMSG '+chan+' :Couldn\'t find anything to enable for: '+arg1+'\r\n')
    else:
      irc.send('PRIVMSG '+chan+' :Argument plz.\r\n')
  if firstmsg == "!disable":
    chan = "#gussi.is"
    try:
      arg1 = usrmsg.split()[1].lower()
    except:
      arg1 = "error"
    if arg1 != "error":
      if arg1 == "seen":
        seenenabled = "false"
        irc.send('PRIVMSG '+chan+' :'+arg1.title()+' disabled succesfully.\r\n')
      elif arg1 == "rekt":
        rektenabled = "false"
        irc.send('PRIVMSG '+chan+' :'+arg1.title()+' disabled successfully.\r\n')
      else:
        irc.send('PRIVMSG '+chan+' :Couldn\'t find anything to enable for: '+arg1+'\r\n')
    else:
      irc.send('PRIVMSG '+chan+' :Argument plz.\r\n')
  if data.lower().find('privmsg #gussi.is') != -1:
    if data.lower().find('<swanmark>') != -1:
      swag = "notswag"
    else:
      seentime = strftime("%H:%M")
      user = data.lower().split('!')[0].replace(':', '')
      if user.lower() != "swanmark" and seenenabled == "true":
        irc.send('PRIVMSG '+chan+' :✓ Seen '+seentime+'\r\n')
