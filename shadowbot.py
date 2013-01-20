import socket
import sys
import string
import irclib

server = "irc.efnet.org"
channel = "#channel"
botnick = "ShadowBot"
version = "ShadowBot 0.0.1a"
readbuffer=""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :ShadowCore IRC Bot 0.0.1\n")
irc.send("NICK "+ botnick +"\n")
irc.send("JOIN "+ channel +"\n")

while 1:
   text=irc.recv(2040)
   print text
   if text.find('PING') != -1:
      irc.send('PONG ' + text.split() [1] + '\r\n')
   if text.find('!version') !=-1:
    irc.send("PRIVMSG "+channel+" :+version+ \r\n")

# Handle a CTCP query
def handleCTCP ( connection, event ):

   # Check to see if it is a "VERSION" query
   if event.arguments() [ 0 ].upper() == 'VERSION':

      # Reply to the query, giving version information
      connection.ctcp_reply ( event.source().split ( '!' ) [ 0 ], 'VERSION Python-IRCLib' )

# Create and IRC object and add the handler
irc = irclib.IRC()
irc.add_global_handler ( 'ctcp', handleCTCP )
