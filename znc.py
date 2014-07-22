#usr/bin/python
#-*- encoding: utf-8 -*-
import socket
import time
import os
import random
import urllib2
import ssl
import math
import json
from random import randrange
#coinking readings
"""  Commenting this out temporarily, don't want to delete it just jet
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
"""
#endof coinking readings
#gamedata json stuff
#endof gamedata json stuff

#f = os.popen("date")
#now = ''.join(f)
#klukkan = now.split(' ')[3]
#month = now.split(' ')[1]
#day = now.split(' ')[2]
#zone = now.split(' ')[4]
#year = now.split(' ')[5]
nick = "bot1337"
server = "swanmark.gulur.net"
ras = "#coinking"
zncfile = open('/home/swanmark/bot/zncLogin.txt', 'r')
zncpwd = zncfile.read()
zncfile.close()
s0cket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc = ssl.wrap_socket(s0cket)
irc.connect((server, 31337))

irc.write('PASS '+zncpwd+'\r\nNICK '+nick+'\r\nUSER 1 2 3 :4\r\n')

time.sleep(1)
irc.recv(8192)
time.sleep(1)
irc.send('JOIN '+ras+'\r\n')
while True:
  data = irc.recv(8192)
  print (data)
  if data.find('://') != -1:
    try:
      uhhwhat = data.split(':')[-2]
      uhok = data.split(':')[3]
      urlstring = uhhwhat+':'+uhok
      url = urlstring.split(' ')[-1].strip()
      uhhcmd = uhhwhat.split(' ')[-0].strip()
      print uhhcmd
      print url
    except:
      url = "error"
      uhhcmd = "error"
  else:
    urlmsg = "error"
    uhhcmd = "error"
  usrmsg = data.split(':')[-1].strip()
  firstmsg = usrmsg.split(' ')[0]
  if data.find('+o JustBerry') != -1:
    chan = data.split(' ')[2]
    irc.send('PIRVMSG chanserv deop '+chan+' JustBerry\r\n')
  if firstmsg.find('!colors') != -1 or firstmsg.find('!colours') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0031_______________________________________________________________________\r\n')
    irc.send('PRIVMSG '+chan+' :\0031|\0030 0\0031 | 1 |\0032 2\0031 |\0033 3\0031 |\0034 4\0031 |\0035 5\0031 |\0036 6\0031 |\0037 7\0031 |\0038 8\0031 |\0039 9\0031 |\00310 10\0031 |\00311 11\0031 |\00312 12\0031 |\00313 13\0031 |\00314 14\0031 |\00315 15\0031 |\r\n')
  if firstmsg == "!pun":
    chan = data.split(' ')[2]
    puns = open('puns.txt').read().splitlines()
    selectedpun = random.choice(puns)
    irc.send('PRIVMSG '+chan+' :'+selectedpun+' - http://i.imgur.com/EQ8LEwc.png\r\n')
  if firstmsg == "!swan":
    chan = data.split(' ')[2]
    try:
      arg1 = usrmsg.split(' ')[1]
    except:
      arg1 = "ERROR"
    if arg1 == "source":
      irc.send('PRIVMSG '+chan+' :Here you can find my bot\'s source: https://github.com/Swanmark/PyBot | This is my first script/program I\'ve written, ever. Please don\'t hate .. a lot.\r\n')
#COINKING VOTE SHIT
  if firstmsg == "!addcoin" or uhhcmd == "!addcoin":
    if uhhcmd == "!addcoin":
      hasurl = "true"
    elif uhhcmd != "!addcoin":
      hasurl = "false"
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    if hasurl == "false":
      """
      try:
        name = str(usrmsg.split(' ')[1])
        ticker = str(usrmsg.split(' ')[2])
        algo = str(usrmsg.split(' ')[3])
        url = url
#        url = str(usrmsg.split(' ')[4])
      except:
        print "Did not find an argument with command !addcoin"
        try:
          if name != "n/a":
            name = name
        except:
          name = "n/a"
        try:
          if ticker != "n/a":
            ticker = ticker
        except:
          ticker = "n/a"
        try:
          if algo != "n/a":
            algo = algo
        except:
          algo = "n/a"
        irc.send('PRIVMSG '+chan+' :Please use the correct format: !addcoin <name> <ticker> <algorithm> <optional thread url>\r\n')
       """
      irc.send('PRIVMSG '+chan+' :Error: You probably did not provide a thread URL.\r\n')
    elif hasurl == "true":
      try:
        name = str(uhhwhat.split(' ')[1])
        print name
        ticker = str(uhhwhat.split(' ')[2])
        print ticker
        algo = str(uhhwhat.split(' ')[3])
        print algo
        url = url
        print url
      except:
        print "Did not find an argument with command !addcoin"
        try:
          if name != "n/a":
            name = name
        except:
          name = "n/a"
        try:
          if ticker != "n/a":
            ticker = ticker
        except:
          ticker = "n/a"
        try:
          if algo != "n/a":
            algo = algo
        except:
          algo = "n/a"
        try:
          if algo != "n/a":
            url = url
        except:
          url = "n/a"
        irc.send('PRIVMSG '+chan+' :Please use the correct format: !addcoin <name> <ticker> <algorithm> <optional thread url>\r\n')
    try:
      coinfile = open('./coins.txt', 'r')
      coinfileread = str(coinfile.read())
      coinfile.close()
      print "probably managed to read file(DEBUG)"
      if coinfileread.find(name) != -1:
        irc.send('PRIVMSG '+chan+' :This coin has already been added.\r\n')
      elif name != "n/a":
        coinfile = open('./coins.txt', 'a')
        coinfile.write(name+':'+ticker+':'+algo+':'+url+':\n')
        coinfile.close()
        irc.send('PRIVMSG '+chan+' :'+nick+' added coin '+name+'.\r\n')
      name = "n/a"
      ticker = "n/a"
      algo = "n/a"
      url = "n/a"
    except:
      print "Trying to open file for reading/writing, doesn't work."

  if firstmsg.lower() == "!coins":
    chan = data.split(' ')[2]
    try:
      coinfile = open('./coins.txt', 'r')
      coins = coinfile.read()
      coinfile.close()
    except:
      coins = "error"
    if coins != "error":
      with open('./coins.txt', 'r') as coinfile:
        for line in coinfile:
          name = line.split(':')[-0].strip()
          ticker = line.split(':')[1].upper().strip()
          urlread1 = line.split(':')[-2].strip()
          urlread2 = line.split(':')[-3].strip()
          if urlread1 == "-":
            url = "-"
          elif urlread1 != "-":
            url = urlread2+':'+urlread1
          algo = line.split(':')[2].strip()
          irc.send('PRIVMSG '+chan+' :'+name+' ['+ticker+'], algo: '+algo+' | '+url+'\r\n')
          name = "error"
          ticker = "error"
          url = ""
          algo = "error"
          time.sleep(0.2)
  if firstmsg.lower() == "!vote":
    chan = data.split(' ')[2]
    user = data.split('!')[0].lower()
    nick = user.replace(':', '')
    try:
      votedcoin = usrmsg.split(' ')[1].lower()
    except:
      votedcoin = "error"
      irc.send('PRIVMSG '+chan+' :Usage: !vote <cointicker> (examples: !vote doge, !vote rzr, !vote btc)\r\n')
    with open('./coins.txt', 'r') as coinfile:
      for line in coinfile:
        ticker = line.split(':')[1].strip()
        with open('./tempfile.txt', 'a') as temp:
          temp.write(ticker)
    with open('./tempfile.txt', 'r') as temp:
      validcoins = temp.read()
      if validcoins.find(votedcoin) != -1:
        vote = "valid"
      else:
        vote = "invalid"
    if votedcoin != "error" and vote == "valid":
      if os.path.exists('./votes/'+votedcoin+'.txt'): #check if coin has been voted for previously (if file exists)
        with open('./votes/'+votedcoin+'.txt', 'r+') as votefile: #open votefile
          currentvotes = int(votefile.read()) #read current votes
          aftervote = currentvotes + 1 #add one vote to current votes
        if os.path.exists('./votes/users/'+nick+'.txt'): #check if userfile exists
          with open('./votes/users/'+nick+'.txt', 'r+') as userfile:#open userfile
            currentcoins = userfile.read() #read current coin votes
          if currentcoins.find(votedcoin) != -1: #check if coin user is trying to vote for has already been voted for by user
            irc.send('PRIVMSG '+chan+' :You\'ve already voted for '+votedcoin+'.\r\n')
            userok = "notok" #testin stuf
          else:
            with open('./votes/users/'+nick+'.txt', 'a') as userfile: #trying to CREATE userfile, with w+ ??? :/
              userfile.write(votedcoin+'\n') #write coin to userfile, so user can't vote for it again ...
        else:
          with open('./votes/users/'+nick+'.txt', 'w+') as userfile:
            userfile.write(votedcoin+'\n')
          with open('./votes/'+votedcoin+'.txt', 'w+') as writevote:#opening votefile to write vote
            writevote.write(str(aftervote))
            irc.send('PRIVMSG '+chan+' :'+nick.title()+' voted for '+votedcoin.title()+'.\r\n')
      else:
        with open('./votes/'+votedcoin+'.txt', 'w+') as votefile:
          votefile.write("1")
        irc.send('PRIVMSG '+chan+' :'+nick.title()+' voted for '+votedcoin.title()+'\r\n')
#i believe the following is an unnecissary duplicate of above code but it's late and I need to hit the bed, whatever.
        if os.path.exists('./votes/users/'+nick+'.txt'): #check if userfile exists
          with open('./votes/users/'+nick+'.txt', 'r+') as userfile:#open userfile
            currentcoins = userfile.read() #read current coin votes
        else:
          with open('./votes/users/'+nick+'.txt', 'w+') as userfile:
            userfile.write(votedcoin)
    elif vote == "invalid":
      irc.send('PRIVMSG '+chan+' :Could not find coin '+votedcoin+'. Try adding the coin with !addcoin\r\n')
#END OF COINKING VOTE SHIT
#Start of game-thingy
  if firstmsg == "!create":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = str(user.replace(':', '')).lower()
    try:
      f = open('./gamedata/users/'+nick+'.txt', 'r')
      irc.send('PRIVMSG '+chan+' :Profile found: '+nick+', can\'t create again.\r\n')
    except:
      createdata = json.dumps({'level':1, 'xp':"null", 'attack':50, 'defence':50, 'banned':"false"})
      a = open('./gamedata/users/'+nick+'.txt', 'w')
      a.write(createdata)
      a.close()
      irc.send('PRIVMSG '+chan+' :Profile created: '+nick+'!\r\n')
  if firstmsg == "!attack":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = str(user.replace(':', '')).lower()
    try:
      target = usrmsg.split(' ')[1].lower()
    except:
      target = "error"
      irc.send('PRIVMSG '+chan+' :You need to provide a target! This should be a user in the channel or "NPC".\r\n')
    try:
      a = open('./gamedata/users/'+nick+'.txt', 'r')
      jloaded = a.read()
      jload = json.loads(jloaded)
      a.close()
      useratt = jload['attack']
      userdef = jload['defence']
      userlvl = jload['level']
      userexp = jload['xp']
      isbanned = jload['banned']
    except:
      irc.send('PRIVMSG '+chan+' :Failed to read account data. Please create an account by typing !create.\r\n')
      useratt = "error"
      userdef = "error"
      userexp = "error"
      userlvl = "error"
    if target == "npc" and target != "error" and isbanned == "false" and useratt != "error":
      attchance = int(randrange(1, 100))
      print "Attack chance was "+str(attchance)+" and user defence was "+str(userdef)
      if attchance >= userdef and userdef != "error":
        try:
          a = open('./gamedata/users/'+nick+'.txt', 'r')
          print "Trying to calculate experience gains."
          jloaded = a.read()
          print jloaded
          jload = json.loads(jloaded)
          a.close()
          oldxp = jload['xp']
          useratt = jload['attack']
          userdef = jload['defence']
          userlvl = jload['level']
          isbanned = jload['banned']
          e = open('./gamedata/users/'+nick+'.txt', 'w')
          if str(oldxp.strip()) == "null":
            gainedxp = "1"
          else:
            intxp = int(oldxp)
            gainedxp = str(intxp + int(userlvl))
          newjsonstring = json.dumps({'level':userlvl, 'xp':gainedxp, 'attack':useratt, 'defence':userdef, 'banned':isbanned})
          e.write(str(newjsonstring))
          e.close()
          irc.send('PRIVMSG '+chan+' :'+nick+' attacks a NPC! You hit the NPC for '+str(attchance)+', enough to kill it. You gain '+str(userlvl)+' experience.\r\n')
        except:
          irc.send('PRIVMSG '+chan+' :Error. Failed to read account data. Logged.\r\n')
          log = open('./gamedata/logs/errors.txt', 'a')
          getdate = os.popen("date")
          now = ''.join(getdate)
          log.write(now+" - Couldn't read account data from user "+str(nick)+" when user should have an account.\r\n")
          log.close()
      elif attchance <= userdef and userdef != "error":
        irc.send('PRIVMSG '+chan+' :'+nick+' attacks a NPC! The NPC blocks the attack and you gain no experience.\r\n')
    elif isbanned == "true":
      irc.send('PRIVMSG '+chan+' :Sorry, '+nick+'. You are banned.\r\n')
#    elif target != "error" and isbanned == "false":
#      try:
#        a = open('./gamedata/users/'+target+'.txt', 'r')
  if firstmsg.lower() == "!mystats":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = str(user.replace(':', '')).lower()
    try:
      a = open('./gamedata/users/'+nick+'.txt', 'r')
      jloaded = str(a.read())
      jload = json.loads(jloaded)
      a.close()
      useratt = str(jload['attack'])
      userdef = str(jload['defence'])
      userlvl = str(jload['level'])
      userexp = str(jload['xp'])
      isbanned = str(jload['banned'])
    except:
      irc.send('PRIVMSG '+chan+' :Could not read from your account. Try creating one with !create.\r\n')
      useratt = "error"
      userdef = "error"
      userexp = "error"
      userlvl = "error"
      isbanned = "error"
    if useratt != "error":
      irc.send('PRIVMSG '+chan+' :Attack: '+useratt+', Defence: '+userdef+', Experience: '+userexp.strip()+', Level: '+userlvl+'. Banned? '+str(isbanned)+'.\r\n')
  if firstmsg.lower() == "!ban":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = str(user.replace(':', '')).lower()
    if nick == "swanmark":
      try:
        targetuser = usrmsg.split(' ')[1].lower()
      except:
        targetuser = "error"
        irc.send('PRIVMSG '+chan+' :You need to provide a target user!\r\n')
      if targetuser != "error":
        try:
          a = open('./gamedata/users/'+targetuser+'.txt', 'r')
          jloaded = str(a.read())
          jload = json.loads(jloaded)
          a.close()
          useratt = str(jload['attack'])
          userdef = str(jload['defence'])
          userlvl = str(jload['level'])
          userexp = str(jload['xp'])
          isbanned = str(jload['banned'])
        except:
          isbanned = "error"
          irc.send('PRIVMSG '+chan+' :Couldn\'t read user data.\r\n')
        if isbanned == "true":
          irc.send('PRIVMSG '+chan+' :'+targetuser+' is already banned. To unban type !unban '+targetuser+'.\r\n')
        elif isbanned != "error":
          ban = json.dumps({'level':userlvl, 'xp':userexp, 'attack':useratt, 'defence':userdef, 'banned':"true"})
          try:
            a = open('./gamedata/users/'+targetuser+'.txt', 'w')
            a.write(str(ban))
            a.close()
            leban == "1"
          except:
            irc.send('PRIVMSG '+chan+' :Could not read '+targetuser+'\'s data. Ban failed.\r\n')
            leban == "0"
          if leban != "0":
            irc.send('PRIVMSG '+chan+' :Banned '+targetuser+'.\r\n')
  if firstmsg.lower() == "!unban":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = str(user.replace(':', '')).lower()
    if nick == "swanmark":
      try:
        targetuser = usrmsg.split(' ')[1].lower()
      except:
        targetuser = "error"
        irc.send('PRIVMSG '+chan+' :You need to provide a target user!\r\n')
      if targetuser != "error":
        try:
          a = open('./gamedata/users/'+targetuser+'.txt', 'r')
          jloaded = str(a.read())
          jload = json.loads(jloaded)
          a.close()
          useratt = str(jload['attack'])
          userdef = str(jload['defence'])
          userlvl = str(jload['level'])
          userexp = str(jload['xp'])
          isbanned = str(jload['banned'])
        except:
          isbanned = "error"
          irc.send('PRIVMSG '+chan+' :Couldn\'t read user data.\r\n')
        if isbanned == "false":
          irc.send('PRIVMSG '+chan+' :'+targetuser+' isn\'t banned. To ban type !ban '+targetuser+'.\r\n')
        elif isbanned != "error":
          ban = json.dumps({'level':userlvl, 'xp':userexp, 'attack':useratt, 'defence':userdef, 'banned':"false"})
          try:
            a = open('./gamedata/users/'+targetuser+'.txt', 'w')
            a.write(str(ban))
            a.close()
            leunban == "1"
          except:
            irc.send('PRIVMSG '+chan+' :Could not read '+targetuser+'\'s data. Unban failed.\r\n')
            leunban == "0"
          if leunban != "0":
            irc.send('PRIVMSG '+chan+' :Unbanned '+targetuser+'.\r\n')
  if firstmsg.find('!conversion') != -1:
    chan = data.split(' ')[2]
    try:
      arg = data.split(':')[-1]
      arg1 = arg.split(' ')[1]
      arg2 = arg.split(' ')[2]
      if arg2.find("mile") != -1:
        if arg1.find(",") != -1:
          arg1 = arg1.replace(",", ".")
        irc.send('PRIVMSG '+chan+' :Following is a conversion from miles to kilometers.\r\n')
        irc.send('PRIVMSG '+chan+' :'+str(arg1)+' miles by 1.609 equals '+str(float(arg1)*1.609)+' kilometers. (Rounded!)\r\n')
        arg1 = "error"
        arg2 = "error"
      if arg2.find("km") != -1 or arg2.find("kilometer") != -1:
        if arg1.find(',') != -1:
          arg1 = arg1.replace(',', '.')
        irc.send('PRIVMSG '+chan+' :Following is a conversion from kilometers to miles.\r\n')
        irc.send('PRIVMSG '+chan+' :'+arg1+' kilometers by 0.621 equals '+str(float(arg1)*0.621)+' miles. (Rounded!)\r\n')
        arg1 = "error"
        arg2 = "error"
      if arg2.find('kg') != -1:
        if arg1.find(',') != -1:
          arg1 = arg1.replace(',', '.')
        irc.send('PRIVMSG '+chan+' :Following is a conversion from kilograms(kg) to pounds(lb)\r\n')
        irc.send('PRIVMSG '+chan+' :'+arg1+' kg by 2.2046 equals '+str(float(arg1)*2.2046)+' pounds (Rounded!)\r\n')
      if arg2.find('lb') != -1 or arg2.find('lb') != -1:
        if arg1.find(',') != -1:
          arg1 = arg1.replace(',', '.')
        irc.send('PRIVMSG '+chan+' :Following is a conversion from pounds(lb) to kilograms(kg)\r\n')
        irc.send('PRIVMSG '+chan+' :'+arg1+' kg divided by 2.2046 equals '+str(float(arg1)/2.2046)+' kilograms (Rounded!)\r\n')
      if arg2.find('°f') != -1:
        if arg1.find(',') != -1:
          arg1 = arg1.replace(',', '.')
        irc.send('PRIVMSG '+chan+' :Following is a conversion from Fahrenheit(°f) to celsius(°c)\r\n')
        irc.send('PRIVMSG '+chan+' :('+arg1+'-32)°f divided by 1.8 equals '+str((float(arg1)-32)/1.8)+'°c\r\n')
      if arg2.find('°c') != -1:
        if arg1.find(',') != -1:
          arg1 = arg1.replace(',', '.')
        irc.send('PRIVMSG '+chan+' :Following is a conversion from Celsius(°c) to Fahrenheit(°f)\r\n')
        irc.send('PRIVMSG '+chan+' :('+arg1+'*1.8)°c + 32 equals '+str((float(arg1)*1.8)+32)+'°f\r\n')
    except:
      irc.send('PRIVMSG '+chan+' :You need to provide two arguments where the first argument only contains numbers, and the second one cotains alphabetical characters. [AMOUNT] [UNITS]\r\n')
      irc.send('PRIVMSG '+chan+' :Units currently available: miles-km, kilograms-pounds, fahrenheit-celsius.\r\n')
  if firstmsg.find('!safezone') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0034► ► ► ► ►\0039SAFE ZONE\0034◄ ◄ ◄ ◄ ◄\r\n')
  if firstmsg.find('!ulilbitch') != -1:
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      if level > 0:
        irc.send('PRIVMSG '+chan+' :What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.\r\n')
        irc.send('PRIVMSG '+chan+' :---\r\n')
        irc.send('PRIVMSG '+chan+' :[Musical] http://youtu.be/NsZMbs5PC64\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 1 or above.\r\n')
    except:
      irc.send('PRIVMSG '+chan+' :Uh oh!\r\n')
  if firstmsg == "!port":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      target = str(usrmsg.split(' ')[1]).strip()
    except:
      target = "error"
      irc.send('PRIVMSG '+chan+' :Missing argument! Argument should be a coin nickname.\r\n')
    try:
      portfile = open('/home/jake/ports.txt', 'r')
      jread = portfile.read()
      portfile.close()
    except:
      irc.send('PRIVMSG '+chan+' :Failed to read data. Sorry.\r\n')
    if target != "error":
      try:
        jsonstr = json.loads(jread)
        tickerport = str(jsonstr[target])
      except:
        tickerport = "error"
      if tickerport != "error":
        irc.send('PRIVMSG '+chan+' :'+target.upper()+' is on port '+tickerport+'.\r\n')
      elif tickerport == "error":
        irc.send('PRIVMSG '+chan+' :'+target.upper()+' is not found in my database.\r\n')
  if firstmsg == "!cinfo":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      target = str(usrmsg.split(' ')[1]).strip()
      try:
        cInfo = str(usrmsg.split(' ')[2]).strip()
      except:
        cInfo = "error"
    except:
      irc.send('PRIVMSG '+chan+' :You need to provide an argument (coin), example "doge" (!cinfo doge)\r\n')
      target = "error"
    try:
      apifile = open('./apikey.txt')
      key = str(apifile.read()).strip()
      print key
      apifile.close()
      jloaded = str(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=coininfo&coin='+target+'&output=json').read())
      jload3d = str(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=poolhashratebycoin&coin='+target+'&output=json').read())
      jload = json.loads(jloaded)
      jl0ad = json.loads(jload3d)
      algo = jload['algo']
      port = jload['port']
      reward = jload['reward']
      blocktime = jload['blocktime']
      diff = jload['difficulty']
      name = jload['name']
      nick = jload['nickname']
      khash = jl0ad['khash']
      mhash = jl0ad['mhash']
      ghash = jl0ad['ghash']
      apierror = "false"
      if name is None:
        exists = "false"
      else:
        exists = "true"
      print exists
      if mhash <= 1000 and mhash >= 1:
        hashrate = str(mhash)+" MH/s"
      elif mhash < 1:
        hashrate = str(khash)+" KH/s"
      elif mhash >= 1000:
        hashrate = str(ghash)+" GH/s"
      else:
        hashrate = "error"
    except:
      irc.send('PRIVMSG '+chan+' :Could not read API.\r\n')
      apierror = "true"
    if apierror != "true" and target != "error" and exists == "true" and cInfo == "error":
      irc.send('PRIVMSG '+chan+' :Coin: '+name+' ['+nick+'] | Port: '+port+' | Algorithm: '+algo+' | Block rewards: '+reward+' | Block time: '+blocktime+' seconds | Diff: '+diff+' | Hashrate: '+hashrate+'.\r\n')
    elif target != "error" and apierror != "true" and exists == "true" and cInfo == "error":
      irc.send('PRIVMSG '+chan+' :You need to provide an argument (coin), example "doge" (!cinfo doge)\r\n')
    elif target != "error" and exists == "false" and cInfo == "error":
      irc.send('PRIVMSG '+chan+' :Coin '+str(target)+' not found!\r\n')
  if firstmsg == "#quiet":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      target = usrmsg.split(' ')[1]
    except:
      print "Did not find an argument with command @quiet"
      target = "error"
    try:
      if level >= 5 and target != "error":
        irc.send('PRIVMSG chanserv op '+chan+'\r\n')
        time.sleep(0.1)
        irc.send('MODE '+chan+' +q '+target+'\r\n')
        irc.send('PRIVMSG chanserv deop '+chan+'\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 5 or above.\r\n')
    except:
      print "Uh oh!"
  if firstmsg == "#unquiet":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      target = usrmsg.split(' ')[1]
    except:
      print "Did not find an argument with command @unquiet"
      target = "error"
    try:
      if level >= 5 and target != "error":
        irc.send('PRIVMSG chanserv op '+chan+'\r\n')
        time.sleep(0.1)
        irc.send('MODE '+chan+' -q '+target+'\r\n')
        irc.send('PRIVMSG chanserv deop '+chan+'\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 5 or above.\r\n')
    except:
      print "Uh oh!"
  if firstmsg == "#op":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      target = usrmsg.split(' ')[1]
    except:
      print "Did not find an argument with command @op"
      target = nick
    try:
      if level >= 7 and target != "error":
        irc.send('PRIVMSG chanserv op '+chan+' '+target+'\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 7 or above.\r\n')
    except:
      print "Uh oh!"
  if firstmsg == "#deop":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      target = usrmsg.split(' ')[1]
    except:
      print "Did not find an argument with command @deop"
      target = nick
    try:
      if level >= 7 and target != "error":
        irc.send('PRIVMSG chanserv deop '+chan+' '+target+'\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 7 or above.\r\n')
    except:
      print "Uh oh!"
  if firstmsg == "#jail":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      target = usrmsg.split(' ')[1]
    except:
      irc.send('PRIVMSG '+chan+' :You need to provide an argument. (user)\r\n')
      target = "error"
    try:
      if level >= 7 and target != "error":
        irc.send('MODE '+chan+' +q '+target+'\r\n')
        irc.send('PRIVMSG '+chan+' :You have been sent to jail! Why don\'t you come over to ##jail and we can talk this through?\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 7 or above.\r\n')
    except:
      print "Uh oh!"
  if firstmsg == "#unjail":
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      target = usrmsg.split(' ')[1]
    except:
      irc.send('PRIVMSG '+chan+' :You need to provide an argument. (user)\r\n')
      target = "error"
    try:
      if level >= 7 and target != "error":
        irc.send('MODE '+chan+' -q '+target+'\r\n')
        irc.send('PRIVMSG '+chan+' :Get out of my cell!\r\n')
        irc.send('KICK ##jail '+target+' :Get out of my cell!\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 7 or above.\r\n')
    except:
      print "Uh oh!"
  if firstmsg.find('!date') != -1:
    f = os.popen("date")
    now = ''.join(f)
    klukkan = now.split(' ')[3]
    month = now.split(' ')[1]
    day = now.split(' ')[2]
    zone = now.split(' ')[4]
    year = now.split(' ')[5]
    chan = data.split(' ')[2]
    if day == 1:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'st of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
    elif day == 2:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'nd of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
    elif day == 3:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'rd of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
    elif day == 21:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'st of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
    elif day == 22:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'nd of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
    elif day == 23:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'rd of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
    else:
      irc.send('PRIVMSG '+chan+' :It is the '+day+'th of '+month+', 2014. Time: '+klukkan+' GMT.\r\n')
  if firstmsg.find('!mod') != -1 and str(data.split('!')[0].replace(':', '')) == "Swanmark":
    user = data.split('!')[0]
    nick = user.replace(':', '')
    chan = data.split(' ')[2]
    try:
      userarg = usrmsg.split(' ')[1]
      level = usrmsg.split(' ')[2]
    except:
      irc.send('PRIVMSG '+chan+' :I need two arguments! [NICK] [LEVEL]!\r\n')
    try:
      f = open('./users/'+userarg+'.txt', 'w')
      f.write(level)
      f.close()
      irc.send('PRIVMSG '+chan+' :'+userarg+' is now level '+str(level)+'.\r\n')
    except:
      irc.send('PRIVMSG '+chan+' :Something went wrong.\r\n')

  if firstmsg.find('!level5only') != -1:
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      print (level)
      f.close()
    except:
      
      irc.send('PRIVMSG '+chan+' :Error: Could not open user info.\r\n')
    try:
      if level > 4:
        irc.send('PRIVMSG '+chan+' :Success! You are level 5 or above.\r\n')
        level = 0
      else:
        irc.send('PRIVMSG '+chan+' :Failure. You are not level 5 or above.\r\n')
    except:
      irc.send('PRIVMSG '+chan+' :Uh oh!\r\n')
  if firstmsg.find('!getlevel') != -1:
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      userarg = usrmsg.split(' ')[1]
    except:
      print "Did not find an argument with command !getlevel"
      userarg = "error"
    try:
      if userarg != "error":
        f = open('./users/'+userarg+'.txt', 'r')
        level = int(f.read())
        f.close()
        irc.send('PRIVMSG '+chan+' :'+userarg+' is currently level '+str(level)+'.\r\n')
      else:
        f = open('./users/'+nick+'.txt', 'r')
        level = int(f.read())
        f.close()
        irc.send('PRIVMSG '+chan+' :You are level '+str(level)+'.\r\n')
    except:
      irc.send('PRIVMSG '+chan+' :Level requested not found.\r\n')
  if firstmsg.find('!irc') != -1:
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = user.replace(':', '')
    try:
      userarg1 = usrmsg.split(' ')[1]
      userarg2 = usrmsg.split(' ')[2]
    except:
      irc.send('PRIVMSG '+chan+' :I need two arguments for this to work. First argument should be (join/part). Second argument should be a channel. (Example #coinking)\r\n')
      userarg1 = "error"
      userarg2 = "error"
    try:
      f = open('./users/'+nick+'.txt', 'r')
      level = int(f.read())
      f.close()
    except:
      irc.send('PRIVMSG '+chan+' :Could not read access level. Ask Swanmark about it.\r\n')
      level = "error"
    if level != "error" and level > 2 and userarg1 != "error" and userarg2 != "error":
      if userarg1 == "join":
        irc.send('JOIN '+userarg2+'\r\n')
        irc.send('PRIVMSG '+chan+' :Joined '+userarg2+'.\r\n')
      elif userarg1 == "part":
        irc.send('PART '+userarg2+'\r\n')
        irc.send('PRIVMSG '+chan+' :Parted from '+userarg2+'.\r\n')
      else:
        irc.send('PRIVMSG '+chan+' :Shit went wrong. Don\'t know what, but shit went horribly wrong.\r\n')
  if data.find('PRIVMSG #') != -1:
    user = data.split('!')[0]
    nick = user.replace(':', '')
    chan = data.split(' ')[2]
    msg = data.split(':')[-1]
    log = open('./logs/'+chan+'.txt', 'a')
    log.write(nick+': '+msg)
    log.close()
  if data.find('JOIN #coinking')  != -1:
    user = data.split('!')[0]
    nick = user.replace(':', '')
    if nick == "jnasm77":
      irc.send('MODE #coinking +v '+nick+'\r\n')
  if firstmsg.find('!clap') != -1:
    user = data.split('!')[0]
    nick = user.replace(':', '')
    chan = data.split(' ')[2]
    try:
      yolomsg = usrmsg.split(' ')[1]
    except:
      print "nothing"
    try:
      irc.send('PRIVMSG '+chan+' :\0039Everyone put your hands together for \0038>>>>>\0034'+yolomsg+'\0038<<<<<\0039!\r\n')
      yolomsg = "error"
    except:
      irc.send('PRIVMSG '+chan+' :\0039Everyone put your hands together for \0038>>>>>\0034'+nick+'\0038<<<<<\0039!\r\n')
########### FLAAAAAAAAGS!
  if firstmsg.find('!flagme') != -1:
    chan = data.split(' ')[2]
    user = data.split('!')[0]
    nick = str(user.replace(':', ''))
    try:
      flagid = int(usrmsg.split(' ')[1])
    except:
      irc.send('PRIVMSG '+chan+' :You need to specify a flag ID: 1=finland, 2=scotland, 3=england.\r\n')
      flagid = 0
    if flagid != "0":
      if flagid == 1:
        irc.send('PRIVMSG #coinking :finland\r\n')
        irc.send('PRIVMSG '+chan+' :\0030'+nick+'\00312'+nick+'\0030'+nick*2+'\r\n')
        irc.send('PRIVMSG '+chan+' :\00312'+nick*4+'\r\n')
        irc.send('PRIVMSG '+chan+' :\0030'+nick+'\00312'+nick+'\0030'+nick*2+'\r\n')
      elif flagid == 2:
        irc.send('PRIVMSG '+chan+' :\0030'+nick+'\0032'+nick+'\0030'+nick+'\r\n')
        irc.send('PRIVMSG '+chan+' :\0032'+nick+'\0030'+nick+'\0032'+nick+'\r\n')
        irc.send('PRIVMSG '+chan+' :\0030'+nick+'\0032'+nick+'\0030'+nick+'\r\n')
      elif flagid == 3:
        irc.send('PRIVMSG '+chan+' :\0030'+nick+'\0035'+nick+'\0030'+nick+'\r\n')
        irc.send('PRIVMSG '+chan+' :\0035'+nick*3+'\r\n')
        irc.send('PRIVMSG '+chan+' :\0030'+nick+'\0035'+nick+'\0030'+nick+'\r\n')
    else:
      irc.send('PRIVMSG '+chan+' :'+nick+'\'s argument returned an error:'+userflag+' Try again.\r\n')
#  if firstmsg.find('!scotlandme'):
#    chan = data.split(' ')[2]
#    user = data.split('!')[0]
#    nick = str(user.replace(':', ''))
#    irc.send('PRIVMSG '+chan+' :\0030'+nick+'\00312'+nick*3+'\0030'+nick+'\r\n')
#    irc.send('PRIVMSG '+chan+' :\00312'+nick*2+'\0030'+nick+'\00312'+nick*2+'\r\n')
#    irc.send('PRIVMSG '+chan+' :\0030'+nick+'\00312'+nick*3+'\0030'+nick+'\r\n')
  if firstmsg == "!holland":
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0034###############\r\n')
    irc.send('PRIVMSG '+chan+' :\0030###############\r\n')
    irc.send('PRIVMSG '+chan+' :\00312###############\r\n')
  if firstmsg.find('!spain') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0034###############\r\n')
    irc.send('PRIVMSG '+chan+' :\0038###############\r\n')
    irc.send('PRIVMSG '+chan+' :\0038###############\r\n')
    irc.send('PRIVMSG '+chan+' :\0034###############\r\n')
  if firstmsg.find('!swe') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\00312###\0038##\00312#####\r\n')
    irc.send('PRIVMSG '+chan+' :\0038##########\r\n')
    irc.send('PRIVMSG '+chan+' :\00312###\0038##\00312#####\r\n')
  if firstmsg.find('!finland') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0030PUU\00312UU\0030UUUZA\r\n')
    irc.send('PRIVMSG '+chan+' :\00312PUUUUUUUZA\r\n')
    irc.send('PRIVMSG '+chan+' :\0030PUU\00312UU\0030UUUZA\r\n')
  if firstmsg.find('!england') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0030####\0035##\0030####\r\n')
    irc.send('PRIVMSG '+chan+' :\0035##########\r\n')
    irc.send('PRIVMSG '+chan+' :\0030####\0035##\0030####\r\n')
  if firstmsg.find('!iceland') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0032###\0030#\0035#\0030#\0032########\r\n')
    irc.send('PRIVMSG '+chan+' :\0030####\0035#\0030#########\r\n')
    irc.send('PRIVMSG '+chan+' :\0035##############\r\n')
    time.sleep(1)
    irc.send('PRIVMSG '+chan+' :\0030####\0035#\0030#########\r\n')
    irc.send('PRIVMSG '+chan+' :\0032###\0030#\0035#\0030#\0032########\r\n')
  if firstmsg.find('!usa') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :http://www.wallpapers-hd.in/wp-content/uploads/2013/11/Jordan-Carver-With-American-Flag-Wallpaper-hd.jpg\r\n')
  if firstmsg == "!germiny":
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :\0031#########\r\n')
    irc.send('PRIVMSG '+chan+' :\0035#########\r\n')
    irc.send('PRIVMSG '+chan+' :\0037#########\r\n')
########## NOMOREFLAGS
  if data.find('DANGER') != -1:
    chan = data.split(' ')[2]
    nickt = data.split('!')[0]
    nick = nickt.replace(':', '')
    if nick == "MrBotterson":
      time.sleep(0.5)
#      irc.send('PRIVMSG '+chan+' :\0038,1IS IT HOT IN HERE OR IS IT JUST THE\0034,1 DAAAANGEEEER \0038,1MRBOTTERSON IS CAUSING?\r\n')
      irc.send('PRIVMSG '+chan+' \0037► ► ► ► ► \0039SAFE   ZONE\0037 ◄ ◄ ◄ ◄ ◄\r\n')
  if firstmsg.find('!redme') != -1:
    chan = data.split(' ')[2]
    nickt = data.split('!')[0]
    nick = nickt.replace(':', '')
    irc.send('PRIVMSG '+chan+' :\0034,1'+nick+'!\r\n')
  if firstmsg.find('!rekt') != -1:
    chan = data.split(' ')[2]
    irc.send('PRIVMSG '+chan+' :☑ rekt ☐ not rekt\r\n')
  if usrmsg.find('s/pewpewppewpewpwepewpwedisabledlololol') != -1:
    asdf = usrmsg.split('s/')[1]
    nickt = data.split('!')[0]
    nick = nickt.replace(':', '')
    chan = data.split(' ')[2]
    print (chan+': '+nick+': '+asdf)
    try:
      log = open('./logs/'+chan+'.txt', 'r')
      lst = log.readlines()
      things = lst[len(lst)-2]
      log.close()
      print ('logs: '+str(things))
      dada = str(things)
      if str(things).split(':')[0] == nick: #make this shit check last three lines
        beforeslash = dada.split('/')[1]
        afterslash = dada.split('/')[-1]
        print (beforeslash+'/'+afterslash)
        wrongmsg = dada.split(':')[-1]
        if dada.find(beforeslash) != -1:
          test1 = str(wrongmsg.split(beforeslash)[1])
          test2 = str(wrongmsg.split(beforeslash)[-1])
          irc.send('PRIVMSG '+chan+' :'+nick+': '+test1+'\r\n')
          irc.send('PRIVMSG '+chan+' :'+test2+'\r\n')
    except:
      print "no"
  if data.find('PRIVMSG #swagchan') != -1:
    msg = str(data.split(':')[2])
    nickt = data.split('!')[-0]
    nick = nickt.replace(':', '')
    if nick != "Swanmark":
      if msg.find('!tip') != -1:
        irc.send('PRIVMSG #swagchan :Oh no you don\'t :D\r\n')
      else:
        irc.send('PRIVMSG #swagchan :'+msg+'\r\n')
  if data.find('!error') != -1:
    nickt = data.split('!')[-0]
    nick = nickt.replace(':', '')
    chan = data.split(' ')[2]
    if nick == "Swanmark":
      irc.send('PRIVMSG '+chan+' :!price h\r\n')
      irc.send('PRIVMSG '+chan+' :!price ho\r\n')
      irc.send('PRIVMSG '+chan+' :!price hom\r\n')
      irc.send('PRIVMSG '+chan+' :!price homo\r\n')
      irc.send('PRIVMSG '+chan+' :!price :D\r\n')
#  if data.find('PRIVMSG #coinking') != -1:
#    nickt = data.split('!')[-0]
#    nick = nickt.replace(':', '')
#    shit = randrange(0, 100)
#    strshit = str(shit)
#    intshit = int(shit)
#    print (strshit)
#    if strshit == "0":
#      strshit = "1"
#    if intshit < 5:
#      if nick != "Swanmark":
#        if nick != "kingtip":
#          if nick != "Shibe_Wanders":
#            if nick != "MrBotterson":
#              if randrange(0, 100) > 95:
#                strshit = str(randrange(100, 500))
#                print "I SHOULD PROBABLY TIP NOW"
#                irc.send('PRIVMSG #coinking :!silenttip '+nick+' '+strshit+' (0.25% chance)\r\n')
#              else:
#                irc.send('PRIVMSG #coinking :!silenttip '+nick+' '+str(int(strshit) * 4)+' (5% chance)\r\n')
  if data.find('PING') != -1:
    irc.send('PONG ' +data.split()[1]+'\r\n')
  if data.find('.block#') != -1:
    chan = data.split(' ')[2]
    if chan != '#dogecoin':
      asdf = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/getblockcount").read()
      irc.send('PRIVMSG '+chan+' :Current dogecoin block: '+asdf+'\r\n')
  if data.find('.diff') != -1:
    chan = data.split(' ')[2]
    if chan != '#dogecoin':
      asdf = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/getdifficulty").read()
      irc.send('PRIVMSG '+chan+' :Current dogecoin difficulty: '+asdf+'\r\n')
  if data.find('.totaldoge') != -1:
    chan = data.split(' ')[2]
    if chan != '#dogecoin':
      asdf = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/totalbc").read()
      irc.send('PRIVMSG '+chan+' :Total dogecoins ever mined: '+asdf+'\r\n')
  if data.find('.balance') != -1:
    arg = data.split(':')[-1]
    arg1 = arg.split(' ')[-1]
    chan = data.split(' ')[2]
    if chan != '#dogecoin':
      try:
        balt = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/addressbalance/"+arg1).read()
        bal = str(balt)
        if bal.find('ERROR') == -1:
          irc.send('PRIVMSG '+chan+' :Address has '+bal+' DOGE.\r\n')
        else:
          irc.send('PRIVMSG '+chan+' :Something went wrong.[else}\r\n')
      except:
        irc.send('PRIVMSG '+chan+' :Something went wrong.[except]\r\n')
  if data.find('.received') != -1:
    arg = data.split(':')[-1]
    arg1 = arg.split(' ')[-1]
    chan = data.split(' ')[2]
    if chan != '#dogecoin':
      try:
        balt = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/getreceivedbyaddress/"+arg1).read()
        print(balt)
        bal = str(balt)
        if bal.find('ERROR') == -1:
          irc.send('PRIVMSG '+chan+' :Since address has been created, it has recieved '+bal+' DOGE.\r\n')
        else:
          irc.send('PRIVMSG '+chan+' :Something went wrong.\r\n')
      except:
        irc.send('PRIVMSG '+chan+' :Something went wrong.\r\n')
  if data.find('.sent') != -1:
    arg = data.split(':')[-1]
    arg1 = arg.split(' ')[-1]
    chan = data.split(' ')[2]
    if chan != '#dogecoin':
      try:
        asdf = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/getsentbyaddress/"+arg1).read()
        bal = str(asdf)
        if bal.find('ERROR') == -1:
          irc.send('PRIVMSG '+chan+' :Since address has been created, it has sent '+bal+' DOGE.\r\n')
        else:
          irc.send('PRIVMSG '+chan+' :Something went wrong.[ELSE]\r\n')
      except:
        irc.send('PRIVMSG '+chan+' :Something went wrong.[EXCEPT]\r\n')
  """ Commenting this out temporarily, don't want to delete it just jet
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
  """
