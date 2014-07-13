import socket
import time
import os
from random import randrange
import json

#coinking readings
a = open('/home/swanmark/python/coinking/data/scrypt.txt', 'r')
b = open('/home/swanmark/python/coinking/data/scryptn.txt', 'r')
c = open('/home/swanmark/python/coinking/data/sha256.txt', 'r')
d = open('/home/swanmark/python/coinking/data/x11.txt', 'r')
e = open('/home/swanmark/python/coinking/data/x13.txt', 'r')
scrypt_old = a.read()
scryptn_old = b.read()
sha256_old = c.read()
x11_old = d.read()
x13_old = e.read()
a.close()
b.close()
c.close()
d.close()
e.close()
try:
  jScrypt_old = json.loads(scrypt_old)
  scrypt_oldname = jScrypt_old['name']
  scrypt_oldnick = jScrypt_old['nickname']
  scrypt_olddiff = str(jScrypt_old['difficulty'])
  scrypt_oldhash = str(jScrypt_old['hashrate'])
except:
  print "STARTUP ERROR: JSON FORMAT: "+scrypt_old
try:
  jScryptn_old = json.loads(scryptn_old)
  scryptn_oldname = jScryptn_old['name']
  scryptn_nick = jScryptn_old['nickname']
  scryptn_diff = str(jScryptn_old['difficulty'])
  scryptn_hash = str(jScryptn_old['hashrate'])
except:
  print "STARTUP ERROR: JSON FORMAT"
try:
  jSha256_old = json.loads(sha256_old)
  sha256_oldname = jSha256_old['name']
  sha256_nick = jSha256_old['nickname']
  sha256_diff = str(jSha256_old['difficulty'])
  sha256_hash = str(float(jSha256_old['hashrate'])/1000)
  sha256_mhash = jSha256_old['hashrate']
except:
  print "STARTUP ERROR: JSON FORMAT"
try:
  jX11_old = json.loads(x11_old)
  x11_oldname = jX11_old['name']
  x11_nick = jX11_old['nickname']
  x11_diff = str(jX11_old['difficulty'])
  x11_hash = str(jX11_old['hashrate'])
except:
  print "STARTUP ERROR: JSON FORMAT: "+x11_old
try:
  jX13_old = json.loads(x13_old)
  x13_oldname = jX13_old['name']
  x13_nick = jX13_old['nickname']
  x13_diff = str(jX13_old['difficulty'])
  x13_hash = str(jX13_old['hashrate'])
except:
  print "STARTUP ERROR: JSON FORMAT: "+x13_old
#endof coinking readings

nick = "DogeG0D"
server = "irc.freenode.net"
ras = "#coinking"
rrr = open('./nickservpass.txt', 'r')
nickservpass = str(rrr.read())
rrr.close()
bSize = "8192"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
time.sleep(1)
irc.recv(8192)
irc.send('NICK '+nick+'\r\n')
irc.send('USER Coinz Coinz Coinz :#coinking fun stuff\r\n')
time.sleep(2)
irc.send('JOIN '+ras+'\r\n')
irc.send('PRIVMSG nickserv :IDENTIFY Swanmark '+nickservpass+'\r\n')
irc.send('PRIVMSG chanserv :deop #coinking\r\n')
irc.send('PRIVMSG chanserv :voice #coinking\r\n')
while True:
  data = irc.recv(8192)
  print (data)
  if data.find('PING') != -1:
    irc.send('PONG ' +data.split()[1]+'\r\n')
  usrmsg = data.split(':')[-1].strip()
  firstmsg = usrmsg.split(' ')[0]


  a = open('/home/swanmark/python/coinking/data/scrypt.txt', 'r')
  scrypt_new = a.read()
  a.close()
  try:
    jScrypt = json.loads(scrypt_new)
    scrypt_name = jScrypt['name']
    scrypt_nick = jScrypt['nickname']
    scrypt_hash = str(jScrypt['hashrate'])
    scrypt_diff = str(jScrypt['difficulty'])
  except:
    print "JSON FORMAT ERROR: Scrypt."
  b = open('/home/swanmark/python/coinking/data/scryptn.txt', 'r')
  scryptn_new = b.read()
  b.close()
  try:
    jScryptn = json.loads(scryptn_new)
    scryptn_name = jScryptn['name']
    scryptn_nick = jScryptn['nickname']
    scryptn_hash = str(jScryptn['hashrate'])
    scryptn_diff = str(jScryptn['difficulty'])
  except:
    "JSON FORMAT ERROR: Scrypt-N."
  c = open('/home/swanmark/python/coinking/data/sha256.txt', 'r')
  sha256_new = c.read()
  c.close()
  try:
    jSha256 = json.loads(sha256_new)
    sha256_name = jSha256['name']
    sha256_nick = jSha256['nickname']
    sha256_hash = str(jSha256['hashrate'])
    sha256_diff = str(jSha256['difficulty'])
  except:
    print "JSON FORMAT ERROR: SHA-256."
  d = open('/home/swanmark/python/coinking/data/x11.txt', 'r')
  x11_new = d.read()
  d.close()
  try:
    jX11 = json.loads(x11_new)
    x11_name = jX11['name']
    x11_nick = jX11['nickname']
    x11_hash = str(jX11['hashrate'])
    x11_diff = str(jX11['difficulty'])
  except:
    print "JSON FORMAT ERROR: X-11."
  e = open('/home/swanmark/python/coinking/data/x13.txt', 'r')
  x13_new = e.read()
  e.close()
  try:
    jX13 = json.loads(x13_new)
    x13_name = jX13['name']
    x13_nick = jX13['nickname']
    x13_hash = str(jX13['hashrate'])
    x13_diff = str(jX13['difficulty'])
  except:
    print "JSON FORMAT ERROR: X-13."
  if scrypt_name != scrypt_oldname or firstmsg.find('!multiport') != -1 and float(scrypt_hash) < 1000:
    scrypt_oldname = scrypt_name
    irc.send('PRIVMSG #coinking :\00312Scrypt multiport is now mining\0034 '+scrypt_name+' ['+scrypt_nick+']\00312 - '+scrypt_hash+' MH/s @ diff: '+scrypt_diff+'.\r\n')
  if scrypt_name != scrypt_oldname or firstmsg.find('!multiport') != -1 and float(scrypt_hash) > 1000:
    irc.send('PRIVMSG #coinking :\00312Scrypt multiport is now mining\0034 '+scrypt_name+' ['+scrypt_nick+']\00312 - '+str(round(float(scrypt_hash)/1000, 3))+' GH/s @ diff: '+scrypt_diff+'.\r\n')
    scrypt_oldname = scrypt_name
  if scryptn_name != scryptn_oldname or firstmsg.find('!multiport') != -1 and float(scryptn_hash) < 1000 and float(scryptn_hash) > 1:
    irc.send('PRIVMSG #coinking :\00312Scrypt-N multiport is now mining\0034 '+scryptn_name+' ['+scryptn_nick+']\00312 - '+scryptn_hash+' MH/s @ diff: '+scryptn_diff+'.\r\n')
    scryptn_name = scryptn_oldname
  elif scryptn_name != scryptn_oldname or firstmsg.find('!multiport') != -1 and float(scryptn_hash) > 1000:
    irc.send('PRIVMSG #coinking :\00312Scrypt-N multiport is now mining\0034 '+scryptn_name+' ['+scryptn_nick+']\00312 - '+str(round(float(scryptn_hash)/1000, 3))+' GH/s @ diff: '+scryptn_diff+'.\r\n')
    scryptn_name = scryptn_oldname
  elif scryptn_name != scryptn_oldname or firstmsg.find('!multiport') != -1 and float(scryptn_hash) < 1:
    irc.send('PRIVMSG #coinking :\00312Scrypt-N multiport is now mining\0034 '+scryptn_name+' ['+scryptn_nick+']\00312 - '+str(round(float(scryptn_hash)*1000, 3))+' KH/s @ diff: '+scryptn_diff+'.\r\n')
    scryptn_oldname = scryptn_name
  if sha256_name != sha256_oldname or firstmsg.find('!multiport') != -1 and sha256_mhash < 1000000:
    irc.send('PRIVMSG #coinking :\00312SHA-256 multiport is now mining\0034 '+sha256_name+' ['+sha256_nick+']\00312 - '+str(round(float(sha256_hash)/1000, 3))+' GH/s @ diff: '+sha256_diff+'.\r\n')
    sha256_oldname = sha256_name
  elif sha256_name != sha256_oldname or firstmsg.find('!multiport') != -1 and sha256_mhash > 1000000:
    irc.send('PRIVMSG #coinking :\00312SHA-256 multiport is now mining\0034 '+sha256_name+' ['+sha256_nick+']\00312 - '+str(round(float(float(sha256_hash)/1000)/1000, 3))+' TH/s @ diff: '+sha256_diff+'.\r\n')
    sha256_oldname = sha256_name
  if x11_name != x11_oldname or firstmsg.find('!multiport') != -1 and float(x11_hash) < 1000:
    irc.send('PRIVMSG #coinking :\00312X-11 multiport is now mining\0034 '+x11_name+' ['+x11_nick+']\00312 - '+x11_hash+' MH/s @ diff: '+x11_diff+'.\r\n')
    irc.send('PRIVMSG #coinking-x11 :\00312X-11 multiport is now mining\0034 '+x11_name+' ['+x11_nick+']\00312 - '+x11_hash+' MH/s @ diff: '+x11_diff+'.\r\n')
    x11_oldname = x11_name
  elif x11_name != x11_oldname or firstmsg.find('!multiport') != -1 and float(x11_hash) > 1000:
    irc.send('PRIVMSG #coinking :\00312X-11 multiport is now mining\0034 '+x11_name+' ['+x11_nick+']\00312 - '+str(round(float(x11_hash)/1000, 3))+' GH/s @ diff: '+x11_diff+'.\r\n')
    irc.send('PRIVMSG #coinking-x11 :\00312X-11 multiport is now mining\0034 '+x11_name+' ['+x11_nick+']\00312 - '+str(round(float(x11_hash)/1000, 3))+' GH/s @ diff: '+x11_diff+'.\r\n')
    x11_oldname = x11_name
  if x13_name != x13_oldname or firstmsg.find('!multiport') != -1 and float(x13_hash) < 1000:
    irc.send('PRIVMSG #coinking :\00312X-13 multiport is now mining\0034 '+x13_name+' ['+x13_nick+']\00312 - '+x13_hash+' MH/s @ diff: '+x13_diff+'.\r\n')
    x13_oldname = x13_name
  elif x13_name != x13_oldname or firstmsg.find('!multiport') != -1 and float(x13_hash) > 1000:
    irc.send('PRIVMSG #coinking :\00312X-13 multiport is now mining\0034 '+x13_name+' ['+x13_nick+']\00312 - '+str(round(float(x13_hash)/1000, 3))+' GH/s @ diff: '+x13_diff+'.\r\n')
    x13_oldname = x13_name
  time.sleep(0.01)
