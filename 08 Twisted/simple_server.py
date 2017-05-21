from twisted.internet import protocol, reactor

# Definisikan class untuk protocol yg akan kita buat


class EchoServer(protocol.Protocol):
    # Callback func ketika koneksi berhasil dibuat
    def connectionMade(self):
        print "Koneksi baru berhasil dibuat"

    # Callback func ketika ada message masuk dari client
    def dataReceived(self, data):
        print data
        data = "OK " + data
        # Kirim balik ke client
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, address):
        return EchoServer()

reactor.listenTCP(7777, EchoFactory())
reactor.run()
