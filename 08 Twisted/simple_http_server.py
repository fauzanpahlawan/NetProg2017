from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

# Define class for protocol


class echoServer(LineReceiver):
    first_line = True
    method = ''
    content_length = 0
    content = ''
    # Connection callback function

    def connectionMade(self):
        print "New connection has been made"

    # Incoming data callback
    def lineReceived(self, data):
        print data
        if self.first_line:
            parsed_data = data.split(' ')
            self.method = parsed_data[0]
            self.first_line = False
        else:
            parsed_data = data.split(": ")
            if parsed_data[0] == "Content-Length":
                self.content_length = int(parsed_data[1])

        # After read header
        if not data:
            self.first_line = True
            # make a condition if the request was GET
            if self.method == "GET":
                print str(self.content_length) + " Content-Length"
                body = "Hello darkness"
                content_len = len(body)
                self.sendResponse(body)
            # to handle POST request which contain content we need to read with
            # rawmode.
            elif self.method == "POST":
                # reset contentS
                self.content = ''
                # switch to rawmode
                self.setRawMode()

    def rawDataReceived(self, data):
        self.content = self.content + data

        if len(self.content) >= self.content_length:
            # switch to line mode
            self.setLineMode()
            # send response to client
            self.sendResponse("Your data: " + self.content + "  ")

    def sendResponse(self, body):
        content_len = len(body)
        self.transport.write("HTTP/1.1 200 OK\r\n")
        self.transport.write("Content-Length: " + str(content_len) + "\r\n")
        self.transport.write("\r\n")
        self.transport.write(body)


# Define class for Factory
class echoFactory(protocol.Factory):
    def buildProtocol(self, address):
        return echoServer()

reactor.listenTCP(7777, echoFactory())
reactor.run()


# resource
# site
# reactor
