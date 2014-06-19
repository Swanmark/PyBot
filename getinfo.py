import urllib2
import time
apifile = open('./apikey.txt', 'r')
key = apifile.read().strip()
apifile.close()
while True:

  try:
    #scrypt
    a = open('./data/scrypt.txt', 'w')
    a.write(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=currentscryptcoin&output=json').read())
    a.close()
    print "Got scrypt data!"
    #scrypt-n
    b = open('./data/scryptn.txt', 'w')
    b.write(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=currentscryptncoin&output=json').read())
    b.close()
    print "Got scrypt-n data!"
    #sha-256
    c = open('./data/sha256.txt', 'w')
    c.write(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=currentsha256coin&output=json').read())
    c.close()
    print "Got sha-256 data!"
    #x-11
    d = open('./data/x11.txt', 'w')
    d.write(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=currentx11coin&output=json').read())
    d.close()
    print "Got x-11 data!"
    e = open('./data/x13.txt', 'w')
    e.write(urllib2.urlopen('https://coinking.io/api.php?key='+key+'&type=currentx13coin&output=json').read())
    e.close()
    print "Got X-13 data!"
    time.sleep(1)
    print "Waiting for 60 seconds to refresh data ..."
  except:
    print "Whoopzie"
  time.sleep(60)
