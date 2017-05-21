from twisted.internet import protocol, reactor

# define a protocol handling class


class EchoServer(protocol.Protocol):
    # Callback func when connection established
    def connectionMade(self):
        print "New connection established."

    # Callback func when client seding a message
    def dataReceived(self, data):
        print data
        data = "OK " + data
        # Kirim balik ke client
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, address):
        return EchoServer()

# reactor so our server will listen on port 7777, and create an instance
# of server with EchoFactory
reactor.listenTCP(7777, EchoFactory())
# finally run the server
reactor.run()
