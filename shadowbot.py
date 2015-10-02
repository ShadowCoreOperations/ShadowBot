#!/usr/bin/python
import socket
import sys
import string

server = "efnet.port80.se"
port = 6667
channel = "#shadowcore"
botnick = "ShadowBot"
realname = "ShadowCore info bot 0.0.1"
ident = "sbot"
readbuffer=""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, port))
irc.send("USER "+ ident +" "+ server +" Name: "+realname+"\n")
irc.send("NICK "+ botnick +"\n")
irc.send("JOIN "+ channel +"\n")

while 1:
   text=irc.recv(2040)
   print text
   if text.find('PING') != -1:
      irc.send('PONG ' + text.split() [1] + '\r\n')
   if text.find('!version') !=-1:
    irc.send("PRIVMSG "+channel+" :+version+ \r\n")
