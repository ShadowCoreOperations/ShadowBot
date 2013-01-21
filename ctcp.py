import sys
import bot

def start():
    print "Module to handle CTCP-requests ..."
    return ctcpfunc

def ctcpfunc(message, sendMessage, dbaccess):
    # response to VERSION querys
    if message["text"] == u"\u0001VERSION\u0001":
        bv = bot.version
        sendMessage(text = u"\u0001VERSION ShadowBot " \
                    u"Version: %s.%s.%s - " \
                    u"(http://www.shadowcore.eu)\u0001" \
                    % (bv["major"], bv["minor"], bv["subbuild"]), \
                     receiver = message["sender"],
                     msgtype="NOTICE")
    #response to PING querys
    elif message["text"].startswith(u"\u0001PING"):
        sendMessage(text = message["text"],
                    receiver = message["sender"],
                    msgtype="NOTICE")
